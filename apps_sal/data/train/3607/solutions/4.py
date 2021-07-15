def eq_sum_powdig(hMax, exp):
    list=[]
    for n in range(100,hMax+1):
        product=0
        for l in str(n):
            product += int(l)**exp
        if n == product:
            list.append(n)
    return list
