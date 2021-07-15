def balanced_num(number):
    a = str(number)
    if len(a)%2!=0:
        n = len(a)//2
        sum1 = 0
        sum2 = 0
        for i in range(n):
            sum1 += int(a[i])
        for i in range(n+1,len(a)):
            sum2 += int(a[i])
        if sum1 == sum2:
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        n = len(a)//2
        sum1 = 0
        sum2 = 0
        for i in range(n-1):
            sum1 += int(a[i])
        for i in range(n+1,len(a)):
            sum2 += int(a[i])
        if sum1 == sum2:
            return "Balanced"
        else:
            return "Not Balanced"
