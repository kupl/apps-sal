def isDigit(string):
    return string.lstrip('-').replace('.','',1).isnumeric()

