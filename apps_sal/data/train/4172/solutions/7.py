import re
def solve(s):
    while '()' in s : s=re.sub(r'\(\)','',s)
    ss = re.sub(r'\(\(|\)\)','',s)
    sss = re.sub(r'\)\(','',ss)
    return [-1,(len(s)-len(ss))//2+len(ss)][not bool(sss)]
