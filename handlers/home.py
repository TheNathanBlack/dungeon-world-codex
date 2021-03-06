import webapp2
import jinja2
from google.appengine.ext import db
from google.appengine.api import users
from data.models import Monster, Profile
import handlers.base
import configuration.site

class HomeHandler(handlers.base.LoggedInRequestHandler):
  """Renders the main page.
  
  Retrieves monsters to be displayed in promotional areas. Currently that
  means the 10 most recent.
  
  Templates used: index.html"""
  
  def get(self):
    """HTML GET handler.
    
    Renders a response to a GET. Queries monsters to feature and renders
    them to the index.html template. Does not accept any query parameters"""
    
    template_values = self.build_template_values()
    template_values['popular_monsters'] = Monster.get_top_rated(5, user=template_values[handlers.base.PROFILE_KEY])
    template_values['recent_monsters'] = Monster.get_recent(5, user=template_values[handlers.base.PROFILE_KEY])
   
    template = configuration.site.jinja_environment.get_template('index.html')
    self.response.write(template.render(template_values))