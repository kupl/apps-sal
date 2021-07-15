import re
def apparently(string):
    return re.sub(r'\b(and|but)\b(?! apparently\b)', r'\1 apparently', string)
