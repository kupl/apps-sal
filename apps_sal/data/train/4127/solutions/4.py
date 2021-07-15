def count_pairs_int(d,n):
    def divs(n):
        x = set()
        for i in range(1,int(n**.5)+1):
            if not n%i:
                x |= {i,n//i}
        return len(x)
        
    c = 0
    for i in range(1,n-d):
        if divs(i) == divs(i+d):
            c += 1
    
    return c
