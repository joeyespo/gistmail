"""
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Use the appropriate environment variable or create a local_config.py instead.
"""

import os


DEBUG = os.environ.get('DEBUG')
HOST = os.environ.get('HOST', 'localhost')
PORT = int(os.environ.get('PORT', 5000))


SPARKPOST_API_KEY = os.environ.get('SPARKPOST_API_KEY')
EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
SENTRY_DSN = os.environ.get('SENTRY_DSN')
