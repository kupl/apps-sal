import re

def check_password(s):
    m = re.match(r'(?=.{8,20}$)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*?])(?=^[a-zA-Z\d!@#$%^&*?]*$)', s)
    return 'valid' if m else 'not valid'
