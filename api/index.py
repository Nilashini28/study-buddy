import sys
import os

# Add server directory to sys.path so its modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server')))

from main import app

app.root_path = "/api"