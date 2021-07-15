import re

def kooka_counter(laughing):
    return len(re.findall(r'(Ha|ha)\1*', laughing))
