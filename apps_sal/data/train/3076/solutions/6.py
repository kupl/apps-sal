def solve(arr):
    
    rev = list(reversed(arr))
    go = []
    direction = 'Begin'
    
    for i in rev:
        nextdirection = i.split(' ')[0]
        go.append(i.replace(nextdirection, direction))
        if nextdirection == 'Left':
            direction = 'Right'
        else:
            direction = 'Left'
            
    return go
        

