import re

def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()    

