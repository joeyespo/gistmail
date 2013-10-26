"""\
GistMail

Email gist@gistmail.com with a link and get a response with that article's summary.
"""

from summarize import summarize_page
from flask import Flask, render_template, request


# Flask application
app = Flask(__name__)
# Configuration
app.config.from_object('settings')
app.config.from_envvar('SETTINGS_MODULE', silent=True)
app.config.from_pyfile('settings_local.py', silent=True)


# Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/incoming', methods=['GET', 'POST'])
def incoming():
    if request.method == 'POST':
        summary = summarize_page()
        # TODO: Email summary
        print summary

    return 'TODO: Implement'


# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug)
