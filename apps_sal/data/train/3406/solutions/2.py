df={0:1}
dm={0:0}
def f(n):
    if n in df: 
        return df[n]
    else:
        df[n]=n-m(f(n-1))
        return df[n]

def m(n):
    if n in dm: 
        return dm[n]
    else:
        dm[n]=n-f(m(n-1))
        return dm[n]
