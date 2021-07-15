import re

def repeating_fractions(q, b):
    return re.sub(r'(\d)\1+(?!\.)', r'(\1)', str(q / b))
