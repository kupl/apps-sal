import re

def get_age(age):
    return int(re.search(r"\d+", age).group())
