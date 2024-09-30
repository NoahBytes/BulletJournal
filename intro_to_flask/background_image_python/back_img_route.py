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

app_id = os.getenv('UNSPLASH_ID')
app_key = os.getenv('UNSPLASH_KEY')
client_secret = os.getenv('UNSPLASH_SECRET')
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""


back_img_blueprint = Blueprint('back_img', __name__)

@back_img_blueprint.route('/back_img',methods=['GET', 'POST'])
@app.route('/back_img',methods=['GET'])
def back_img():  
  py_un = PyUnsplash(api_key=app_key)
  search = py_un.search(type_='photos', page = 1, per_page = 1, query='rain, nature')
  for photo in search.entries:
    photo.refresh()
    returnPhoto = photo.link_download
    print(photo.id, photo.link_download)
  # photo = py_un.photos(type_="single", photo_id='l0_kVknpO2g')
  return returnPhoto
  #print(photo.entries.get_attribution(format='html'))
  #return link.link_download
        # print(f"{response.status_code}")
        # if response.status_code == 200:
        #   data = response.json()
        #   # Extract the image URL (you can choose different sizes if needed)
        #   image_url = data['urls']['regular']  # Use 'full', 'small', etc. as needed
        #   return render_template('home.html', image_url=image_url)
        # else:
        #   return render_template('home.html', image_url=None)
        
