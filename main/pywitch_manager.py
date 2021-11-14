import string
import random
import main.token as tk
from pywitch import (
    validate_token,
    PyWitchHeat
)

valid_char = string.ascii_letters + string.digits

def random_string(length):
    return ''.join([random.choice(valid_char) for i in range(length)])

event_data_click = {}

def heat_callback(data):
    event_id = random_string(16)
    data['event_id'] = event_id
    event_data_click.update(data)

class PyWitchManager():
    def __init__(self):
        self.token = tk.token
        self.channel = 'gleenus'
        self.users = {}
        self.data_click = event_data_click
    
    def start(self):
        self.validation, self.helix_headers = validate_token(self.token)
        self.heat = PyWitchHeat(self.channel, self.token, heat_callback, self.users)
        self.heat.start()
        
#    def get_data(self):
#        self.data = event_data
