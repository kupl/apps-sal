import re
def solve(s):
    
    array = re.findall(r'[0-9]+', s)
    x = [int(i) for i in array]
    x.sort()
    return x[-1] 
