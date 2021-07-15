import random

def random_case(x):
    return "".join([random.choice([c.lower(), c.upper()]) for c in x])
