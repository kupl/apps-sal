import re
def dad_filter(string):
    return re.sub(r'((?<=\,)\,+|[\s,]+\Z)','',string)
