import re

def toUnderScore(name):
    return re.sub("(?<=[^_-])_?(?=[A-Z])|(?<=[^\\d_])_?(?=\\d)", "_" , name)
