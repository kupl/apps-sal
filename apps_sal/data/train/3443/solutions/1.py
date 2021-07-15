from functools import reduce

def correct(m, n, bits):
        
    def getDiff(check,lines):
        return next((i for i,(c,line) in enumerate(zip(check,lines)) if int(c) != reduce(int.__xor__, list(map(int,line)))), -1)

    a = getDiff(bits[-m-n:-n], (bits[i:i+n]   for i in range(0,m*n,n)) )
    b = getDiff(bits[-n:],     (bits[i:m*n:n] for i in range(n)) )
    
    if a+b != -2:
        i    = a*n+b if a+1 and b+1 else -m-n+a if b==-1 else len(bits)-n+b
        bits = f'{ bits[:i] }{ int(bits[i])^1 }{ bits[i+1:] }'
        
    return bits

