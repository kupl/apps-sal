def encode(message, key):
    
    z = [int(i) for i in str(key)]
    x = 0
    sol = []
    
    for i in message:
        
        if x == len(z):
            x = 0
        sol.append(ord(i)-96+z[x])
        x+=1
    
    return sol
