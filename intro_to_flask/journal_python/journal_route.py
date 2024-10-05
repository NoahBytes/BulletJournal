import os
import openai
from openai import OpenAI
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint
from .journal_form import JournalForm

journal_blueprint = Blueprint('journal', __name__)

@journal_blueprint.route('/journal',methods=['GET', 'POST'])
@app.route('/journal',methods=['GET', 'POST'])
def journal():
  form = JournalForm(request.form)
  
  if request.method == 'POST':
      if form.validate() == False:
        return render_template('journal.html', form=form)
      else:
        return render_template('journal.html', success=True)
      
  elif request.method == 'GET':
      return render_template('journal.html', form=form)