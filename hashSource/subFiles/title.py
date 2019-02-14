import os

def title():
    if os.name == 'nt':
        _ = os.system('title Hash Generator V. 1.0')
    else:
        x = 5