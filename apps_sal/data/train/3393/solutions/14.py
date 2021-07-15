def list_squared(m, n):
    output = []
    for i in range(m,n):
        div = set() #using set to ignore duplicates (the square root of i)
        for d in range(1,int(i**0.5)+1): #going up to square root to save time. 
            if i%d == 0:
                div.add(d) #if d is a divisor, i/d is also a divisor
                div.add(i/d)
        sumsqdiv = sum([a * a for a in div]) #using map/lambda to multiply all divisors. 
        if (sumsqdiv**0.5).is_integer():
            output.append([i,sumsqdiv])
    return output

