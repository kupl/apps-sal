def max_number(n):
    num=list(str(n))
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j]<num[j+1]:
                num[j+1],num[j]=num[j],num[j+1]
    large=""
    for i in num:
        large+=i
    return int(large)
