from intro_to_flask import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    greeting = db.Column(db.String(256))

    journal_entries = db.relationship('JournalEntry', backref='author', lazy=True)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Add the UserPreference model here
class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(20), nullable=False, default='light')
    font_size = db.Column(db.String(10), nullable=False, default='medium')
    notifications_enabled = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to link back to the User model
    user = db.relationship('User', backref=db.backref('preferences', lazy=True))
    