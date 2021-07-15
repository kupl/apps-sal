import re

def repeating_fractions(q, b):
    x, y = str(q / b).split('.')
    return x + '.' + re.sub(r'(\d)\1+', r'(\1)', y)
