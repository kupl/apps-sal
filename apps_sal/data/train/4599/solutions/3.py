import re


def owl_pic(text):
    new_string = re.sub('(?i)[^8wtyuioahxvm]', '', text).upper()
    return f"{new_string}''0v0''{new_string[::-1]}"
