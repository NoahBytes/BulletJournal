import os
from flask import jsonify
import requests
import re #regular expressions module
from markupsafe import escape #protects projects against injection attacks
from intro_to_flask import app
import sys 
sys.dont_write_bytecode = True
from flask import render_template, request, Flask, Blueprint

from pyunsplash import PyUnsplash
import datetime
app_id = os.getenv('UNSPLASH_ID')
app_key = os.getenv('UNSPLASH_KEY')
client_secret = os.getenv('UNSPLASH_SECRET')
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

def timeQuery():
  returnVar = ""
  time = datetime.datetime.now()
  if time.hour > 18:
         returnVar = "City, Night"
  elif time.hour > 12:
    returnVar = "Rain, Nature"
  elif time.hour < 12:
        returnVar = "Coffee, Morning"

  return returnVar

back_img_blueprint = Blueprint('back_img', __name__)

@back_img_blueprint.route('/back_img',methods=['GET', 'POST'])
@app.route('/back_img',methods=['GET'])
def back_img(query_var):  
  try:
    if query_var == "":
      query_var = timeQuery()
    py_un = PyUnsplash(api_key=app_key)
    search = py_un.search(type_='photos', page = 1, per_page = 1, query=query_var)
    for photo in search.entries:
      photo.refresh()
      return photo.link_download
  except Exception as e:
     return "static/img/alex-dukhanov-ZxZQk7777R4-unsplash.jpg"
        
