import math as m
def find_baller(s, r):
    count = len(r)
    if count == 1:
        return r[0]
    
    size = 3**(m.ceil(m.log(count,3))-1)
    
    x = size
    if size > count-size:
        x -= 2*size-count
        
    parts = [r[:x] , r[x:-x], r[-x:]]
    
    x = s.get_weight(parts[0], parts[2])+1
    print(x)
    return find_baller(s,parts[x])

def find_ball(s,count):
    return find_baller(s,list(range(count)))
