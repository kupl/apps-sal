def spinning_rings(inner_max, outer_max):
    
    i = inner_max+1
    j = outer_max+1
    
    x = 1
    while x < i*j:
        a = -x % i
        b = x % j
        if a == b:
            return x
        elif a > b: 
            if a > j:
                x += a-j
            else:                
                x+= max((a-b)//2,1)
        elif b > a:
            if b > i:
                x+= j-b
            else:
                x+= max(min(j-b,a),1)
