n, s = list(map(int, input().split()))

a = list(map(int, input().split()))

a.sort()
if(s > a[n // 2]):
    fir = n
    for i in range(n // 2, n):
        if(a[i] >= s):
            fir = i
            break
    sum1 = sum(a[n // 2:fir])
    fin = s * (fir - n // 2)
    print(fin - sum1)
elif(s < a[n // 2]):
    fir = n // 2
    for i in range(n // 2):
        if(a[i] >= s):
            fir = i
            break
    sum1 = sum(a[fir:n // 2 + 1])
    fin = s * (n // 2 - fir + 1)
    print(sum1 - fin)
else:
    print(0)
