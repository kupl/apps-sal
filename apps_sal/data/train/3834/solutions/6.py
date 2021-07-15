def palin(n,pos):
    half = str(int('1'+'0'*(n//2-int(not n&1)))+pos-1)
    full = int(half + [half,half[:-1]][n&1][::-1]) 
    return full
