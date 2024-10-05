import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sys.dont_write_bytecode = True

app = Flask(__name__)

app.secret_key = 'development key'
app.config['SECRET_KEY']='LongAndRandomSecretKey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#mail.init_app(app)

from .routes import mail

from intro_to_flask import models