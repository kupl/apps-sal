def complexSum(arr):
    s = sum(complex(i.replace('i','j')) for i in arr)
    r,i = map(int,(s.real,s.imag))
    return f'{r}' if not i else f"{'-' if i==-1 else '' if i==1 else i}i" if not r else f"{r}{'+' if i>0 else ''}{i}i"
