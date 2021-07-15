import re

def dont_give_me_five(start,end):
    n = 0
    for i in range(start, end + 1):
        if re.match('(.*)[5](.*)', str(i)):
            continue
        n += 1 
    return n
