from re import search

def check_password(s):
    return 'valid' if bool(search('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*?])[\w!@#$%^&*?]{8,20}$', s)) else 'not valid'
