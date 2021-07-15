import re
def password(string):
    
    return bool(re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$",string))
