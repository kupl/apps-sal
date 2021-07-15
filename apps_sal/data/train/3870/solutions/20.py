import re

def solve(s):
    space_index = [m.start() for m in re.finditer(" ",s)]
    reverse = s.replace(" ","")[::-1]
    list_reverse = list(reverse)
    for index in space_index:
        list_reverse.insert(index," ")
    return ''.join(list_reverse)
