import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8578130308:AAEdXrHfDd3SJDr5d5ORqKWi0g3jPyAg_2E')
    API_ID = int(os.environ.get("API_ID", '30744675'))
    API_HASH = os.environ.get("API_HASH", '2b2ab5de1550aaf6e8c4bb91daf8d1cf')
    AUTH_USER = os.environ.get('AUTH_USERS', '5230086079').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "hacker"#Here You Can Change with Your Name  or any custom name or title you prefer

