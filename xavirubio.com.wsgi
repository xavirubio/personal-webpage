import sys
sys.path.insert(0, '/var/www/html/personalwebpage')

activate_this = '/home/pi/.local/share/virtualenvs/personalwebpage-36lbLGT-/bin/activate_this.py'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application