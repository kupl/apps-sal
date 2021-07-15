def max_number(n):
    resfornow = []
    while n>0:
        resfornow.append(n%10)
        n= n//10
    res = ""
    for i in reversed(sorted(resfornow)):
        res+= str(i)
    return int(res)

