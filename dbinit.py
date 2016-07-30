import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlalchemy
from PacktPubSubscription import app

try:
    db_uri = 'mysql://%s:%s@localhost:3306/' % (app.config['DB_USERNAME', 'DB_PASSWORD'])
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE " + app.config['USER_DATABASE_NAME'])
    conn.close()
except:
    print "Database exists"

from PacktPubSubscription import db
from user.models import *

db.create_all()

