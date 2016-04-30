"""
GistMail

Email gist@gistmail.com with a link and get a response with that
article's summary.
"""

from __future__ import print_function, unicode_literals

import re
from email.utils import parseaddr

from flask import Flask, abort, render_template, request
from raven.contrib.flask import Sentry
from sparkpost import SparkPost

from summarize import summarize_page


# Flask application
app = Flask(__name__)
# Configuration
app.config.from_object('settings')
app.config.from_envvar('SETTINGS_MODULE', silent=True)
app.config.from_pyfile('settings_local.py', silent=True)
# Email
sparkpost = SparkPost(app.config['SPARKPOST_API_KEY'])
# Error logging
sentry = Sentry(app) if app.config['SENTRY_DSN'] != 'disabled' else None


# Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    if not bool(app.config['DEBUG']):
        abort(404)
    return render_template('admin.html')


@app.route('/incoming', methods=['POST'])
def incoming():
    from_email = request.form.get('from', '')
    print(' * INCOMING EMAIL from', repr(from_email))

    name, email = parseaddr(from_email)
    subject = request.form.get('subject')
    text = request.form.get('stripped-text')

    # Prevent infinite sends
    if email.lower() == parseaddr(app.config['EMAIL_SENDER'])[1].lower():
        return ''

    # Validation
    if not email or not subject or not text:
        print(' * SKIPPING: Missing "from", "subject", or "text" field.')
        return ''

    # Find the URL
    matches = re.search('(?P<url>https?://[^\s]+)', text)
    url = matches.group('url') if matches else None
    if not url:
        print(' * SKIPPING: No URL found in the provided text.')
        return ''
    print('Summarizing:', url)

    try:
        summary = summarize_page(url)
    except Exception as ex:
        if sentry:
            sentry.captureException()
        print(' * ERROR:', type(ex), ex)
        subject = '[ERROR] ' + subject
        html = render_template('error_email.html', url=url)
    else:
        html = render_template(
            'summary_email.html', title=summary.title, url=summary.url,
            summaries=summary.summaries)

    print('Replying to:', email)
    email_id = send_email(email, subject, html)

    print('Reply ID:', email_id)
    return ''


# Helpers
def send_email(to, subject, html):
    name, email = parseaddr(app.config['EMAIL_SENDER'])
    from_email = {'name': name, 'email': email}

    response = sparkpost.transmission.send(
        recipients=[to], subject=subject, html=html, from_email=from_email)
    return response['id']


# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug)
