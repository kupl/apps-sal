import re

def trump_detector(trump_speech):
    lst = [ len(tup[1]) for tup in re.findall(r'([aeiou])(\1*)', trump_speech, re.I) ]
    return round(sum(lst)/len(lst), 2)
