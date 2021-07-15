import re

def compare(s1,s2):
    if s1 is None or re.match( '^[a-zA-Z]*$', s1) == None : s1 = ''
    if s2 is None or re.match( '^[a-zA-Z]*$', s2) == None : s2 = ''
    return sum(map(ord,s1.upper())) == sum(map(ord,s2.upper()))
