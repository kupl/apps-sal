from random import choice 

LOWER_UPPER = (str.lower, str.upper)

def random_case(text):
    return ''.join(choice(LOWER_UPPER)(c) for c in text)
