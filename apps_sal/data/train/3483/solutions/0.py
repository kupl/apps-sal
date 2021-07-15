import re
def string_parse(string):
    return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'
