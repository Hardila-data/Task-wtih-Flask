import os

#dir where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = "task.db"
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLE = True #r cross-site request forgery
SECRET_KEY = 'taskflask'

#path of database
DATABASE_PATH = os.path.join(basedir, DATABASE)