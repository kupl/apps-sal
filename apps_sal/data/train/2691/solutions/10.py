import re
def solve(s):  
    reg = r"(\+?\-?\ *\d+\.?\d*)" 
    return max(map(float, re.findall(reg, s)))
