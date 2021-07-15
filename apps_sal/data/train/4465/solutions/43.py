def super_size(n):
    num=str(n)
    arr=[]
    for i in range(0,len(num)):
        arr.append(num[i])
    arr.sort(reverse=True)
    return int(''.join(arr))

