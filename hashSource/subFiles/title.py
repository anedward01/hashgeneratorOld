import os

def title():
    if os.name == 'nt':
        _ = os.system('title Hash Generator V. 1.1')
    else:
        x = 5

def version():
    vers = '1.1'
    return vers
