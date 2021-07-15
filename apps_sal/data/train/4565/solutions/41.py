import re

# Don't use a class name like str as an argument name
def replace_dots(str):
    return str.translate(str.maketrans(".", "-"))
    return str.replace(".", "-")
    return re.sub(r"\.", "-", str)
