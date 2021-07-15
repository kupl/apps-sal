def solve(a):
    b= 0
    m= 0 
    for i in range(len(a)):
        if a[i] == a[i].lower() :
            m += 1
        else :
            b += 1
    if m>=b :
        return a.lower()
    else :
        return a.upper()
