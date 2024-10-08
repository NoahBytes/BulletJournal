import os
import openai
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask,Blueprint
from flask_mail import Message, Mail
from .contact_form import ContactForm
from .ask_python.ask_route import ask_blueprint
from .draw_python.draw_route import draw_blueprint
from .journal_python.journal_route import journal_blueprint
from .transcribe_python.transcribe_route import transcribe_blueprint
from intro_to_flask.models import User, UserPreference  # Import the models

#The mail_user_name and mail_app_password values are in the .env file
#Google requires an App Password as of May, 2022: 
#https://support.google.com/accounts/answer/6010255?hl=en&visit_id=637896899107643254-869975220&p=less-secure-apps&rd=1#zippy=%2Cuse-an-app-password

mail_user_name = os.getenv('GMAIL_USER_NAME')
mail_app_password = os.getenv('GMAIL_APP_PASSWORD')
openai.api_key = os.getenv('OPENAI_API_KEY')

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = mail_user_name
app.config['MAIL_PASSWORD'] = mail_app_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  # Flask 2.2.2 requires a parameter to a form object: request.form or other
	# See https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
  form = ContactForm(request.form) 

  if request.method == 'POST':
      if form.validate() == False:
        return render_template('contact.html', form=form)
      else:
        msg = Message(form.subject.data, sender=mail_user_name, recipients=[form.email.data])
        msg.body = """From: %s <%s> \n%s \n%s
        """ % (form.name.data, form.email.data, form.subject.data, form.message.data)
        mail.send(msg)

        return render_template('contact.html', success=True)

  elif request.method == 'GET':
      return render_template('contact.html', form=form)
       
app.register_blueprint(journal_blueprint) 
app.register_blueprint(ask_blueprint) 
app.register_blueprint(draw_blueprint) 
app.register_blueprint(transcribe_blueprint)

# New route for Create operation (Setting User Preferences)
@app.route('/preferences', methods=['POST'])
def set_preferences():
    user_id = request.json.get('user_id')
    theme = request.json.get('theme', 'light')
    font_size = request.json.get('font_size', 'medium')
    notifications_enabled = request.json.get('notifications_enabled', True)

    # Fetch the user by ID
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create and save the user's preferences
    user_preferences = UserPreference(
        theme=theme,
        font_size=font_size,
        notifications_enabled=notifications_enabled,
        user_id=user_id
    )

    db.session.add(user_preferences)
    db.session.commit()

    return jsonify({'message': 'Preferences saved successfully!'})
  
