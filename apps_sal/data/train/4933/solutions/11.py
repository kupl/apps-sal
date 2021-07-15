from random import choice

def random_case(text):
    return ''.join(choice([c.upper(), c.lower()]) for c in text)
