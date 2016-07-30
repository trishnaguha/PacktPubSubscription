SECRET_KEY = 'abgkahalfajjgagw'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'test'
USER_DATABASE_NAME = 'user'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@localhost:3306/%s' % (DB_USERNAME, DB_PASSWORD, USER_DATABASE_NAME)
