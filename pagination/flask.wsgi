import sys, os
sys.path.insert (0,'/var/www/flask')
os.chdir("/var/www/flask")
from index import app as application
