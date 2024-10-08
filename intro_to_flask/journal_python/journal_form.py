import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError

class JournalForm(Form):
    title = TextAreaField("Title",  [validators.InputRequired("Please enter a title for this journal.")])
    content = TextAreaField("Content", id = 'markdown-editor')
    submit = SubmitField("Save") 