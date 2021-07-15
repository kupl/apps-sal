import re

pattern = re.compile('A8A8A8A8A8.-A%8.88.'.replace('A', '[A-Z]').replace('8', '[0-9]').replace('.', r'\.'))

def body_count(code):
    return bool(pattern.search(code))
