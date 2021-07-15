import re
from string import ascii_lowercase as c 
def solve(s):   
    return max([sum(map(lambda x: c.index(x)+1,list(i))) for i in re.findall(r'[^aeiou]+',s)])
