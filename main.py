import cgi
import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.api import users
from google.appengine.ext import db

class Landing(webapp2.RequestHandler):
	def get(self):
		t = jinja_env.get_template('Landing.html')
		self.response.out.write(t.render())

app = webapp2.WSGIApplication([
		('/', Landing)
	], debug=True)

