from collections import Iterable

def unpack(l):
    output = []
    
    queue = l[:]
    while queue:
        x = queue.pop(0)
        
        if type(x) is dict:
            queue.append(x.items())
        elif isinstance(x, Iterable) and type(x) != str:
            for y in x:
                queue.append(y)
        else:
            output.append(x)
                
    return output
