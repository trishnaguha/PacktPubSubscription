from PacktPubSubscription import db

'''
Model description
'''

class User(db.Model):
    """User table"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        """
        Return email id
        Query in db
        """
        return '<Email %r>' % self.email
