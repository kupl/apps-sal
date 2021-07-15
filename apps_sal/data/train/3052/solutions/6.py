import regex

def remove(s):
    return regex.sub(r'!++(?!$)', '', s)
