import re

def clean_string(s):
    return clean_string(re.sub('[^#]{1}#', '', s).lstrip('#')) if '#' in s else s

