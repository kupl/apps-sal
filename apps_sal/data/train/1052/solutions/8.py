t = int(input())

def digisum(a):
    a = str(a)
    x = 0
    for i in a:
        x += int(i)
    return x

for _ in range(0,t):
    x = input()
    n = int(x.split(' ')[0])
    d = int(x.split(' ')[1])
    
    dict = {n:0}
    stop_at = 1
    curr_items = [n]
    next_items = []
    steps = 0
    
    #if n%3 == 0 and d%3 == 0:
     #   stop_at = 3
    
    while stop_at not in dict and steps < 11:
        steps += 1
        for i in curr_items:
            ds = digisum(i) if i >= 10 else 0
            ad = i + d
            
            if ds != 0 and ds not in dict:
                next_items.append(ds)
                dict[ds] = steps
            
            if ad not in dict:
                next_items.append(ad)
                dict[ad] = steps
                
        curr_items,next_items = next_items,[] 
        
    for i in range(1,10):
        if i in dict:
            stop_at = i
            steps = dict[i]
            break
                
    print(stop_at,steps)
            
