"""
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Use the appropriate environment variable or create a local_config.py instead.
"""

import os


DEBUG = os.environ.get('DEBUG')
HOST = os.environ.get('HOST', 'localhost')
PORT = int(os.environ.get('PORT', 5000))


MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')
FROM_EMAIL = os.environ.get('FROM_EMAIL')
FROM_NAME = os.environ.get('FROM_NAME')
SENTRY_DSN = os.environ.get('SENTRY_DSN')
