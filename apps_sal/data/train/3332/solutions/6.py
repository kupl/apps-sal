import re
def autocorrect(input):
    rgx = r'\b([Yy]ou+|u)\b'
    return re.sub(rgx, 'your sister', input)
