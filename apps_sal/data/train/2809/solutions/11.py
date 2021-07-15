import re

def digitize(n):
    answer = []
    l= re.findall('\d', str(n))
    for i in l:
         answer.append (int(i))
    answer.reverse()
    return answer
