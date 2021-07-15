def reverse(right):
    
    left = [right[-1]]
    k=right
    for i in range(len(right)-1):
        k=list(map(lambda x,y:x-y,k,k[1:]))
        left.append(k[-1])
    left.reverse()
            
    return left
