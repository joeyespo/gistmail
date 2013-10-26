"""\
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Use the appropriate environment variable or create a local_config.py instead.
"""

import os


# Server settings
HOST = os.environ.get('HOST', 'localhost')  # Use '0.0.0.0' to expose this externally
PORT = int(os.environ.get('PORT', 5000))    # Use 80 to behave like a standard server
DEBUG = os.environ.get('DEBUG')             # Uses debug mode when run with app.run()
SECRET_KEY = os.environ.get('SECRET_KEY')   # Generate a key to enable secure cookies
SERVER_NAME = os.environ.get('SERVER_NAME') # The external-visible name of the server


# Email settings
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')
MANDRILL_EMAIL = os.environ.get('MANDRILL_EMAIL')
MANDRILL_EMAIL_NAME = os.environ.get('MANDRILL_EMAIL_NAME')


# Error logging settings
SENTRY_DSN = os.environ.get('SENTRY_DSN')
SENTRY_DISABLED = os.environ.get('SENTRY_DISABLED')
