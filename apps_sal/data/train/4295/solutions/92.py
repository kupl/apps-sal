def balanced_num(n):
    print(n)
    b = list(str(n))
    a = [int(x) for x in b] 
    c = len(a)
    if c == 1 or c == 2 : return "Balanced"
    if c % 2 == 0: 
        a.pop(c//2)
        c -= 1
    return "Balanced" if sum(a[:c//2]) == sum(a[c//2+1:]) else "Not Balanced"
