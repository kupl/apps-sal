import re

def apparently(string):
    return re.sub(r'(?<=\b(and|but)\b(?! apparently\b))', ' apparently', string)
