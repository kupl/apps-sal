import re
def solve(s):
    s = re.sub('[^0-9]+', 'x', s)
    l = s.split('x')
    res = []
    for i in l:
        if(i is ''):
            pass
        elif i.isnumeric:
            res.append(int(i))
    return(max(res))
    

