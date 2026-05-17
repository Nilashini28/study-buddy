import os
import sys

# Add the 'server' directory to the Python path so absolute imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'server'))

from main import app
