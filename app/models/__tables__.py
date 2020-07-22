from app import db


class User(db.model):
    __tablename__ = "users"
    id = db.collumn(db.Interger, primary_key=True)
    name = db.collumn(db.String(80))
    email = db.collumn(db.String(120), unique=True)
    password = db.collumn(db.String(20), unique=True)

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.model):
    __tablename__ = "posts"

    id = db.collumn(db.Interger, primary_key=True)
    content = db.collumn(db.text)
    users_id = db.collumn(db.Interger, db.Foreinkey('users.id'))

    user = db.relationship('User', Foreign_keys=users_id)

    def __init__(self, content, user_id):
        self.content = content
        self.users_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.model):
    __tablename__ = "follow"

    id = db.collumn(db.Interger, primary_key=True)
    user_id = db.collumn(db.Interger, db.Foreinkey('users.id'))
    follower_id = db.collumn(db.Interger, db.Foreinkey('users.id'))

    users = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=user_id)
