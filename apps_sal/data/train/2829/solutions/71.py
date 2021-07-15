def array_madness(a,b):
    sum1=0
    sum2=0
    for i in range(len(a)):
        sum1=sum1+(a[i]**2)
    for j in range(len(b)):
        sum2=sum2+(b[j]**3)
    if sum1>sum2:
        return True
    else:
        return False
