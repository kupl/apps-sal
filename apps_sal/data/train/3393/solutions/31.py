def list_squared(m, n):
    lst = []
    for num in range(m, n):
        s = set()
        for div in range(1, int(num**0.5)+1):
            if not num%div: s.update({div**2, int(num/div)**2})
        summ = sum(s)
        if ((summ**0.5)//1)**2 == summ: lst.append([num, summ])
    return lst
    

