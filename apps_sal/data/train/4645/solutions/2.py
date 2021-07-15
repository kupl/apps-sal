
def next(last_l, last_r):
    return last_l[0] + last_r[0], last_l[1] + last_r[1]

def promenade(choices):
    last_l = (1, 0)
    last_r = (0, 1)
    last = None
    
    for c in choices:
        if c == "L":
            last_l = next(last_l, last_r)
        else:
            last_r = next(last_l, last_r)
            
    return next(last_l, last_r)
            
        
    
    
    # good luck!

