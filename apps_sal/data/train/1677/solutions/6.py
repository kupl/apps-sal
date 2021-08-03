# cook your dish here
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
ssum = 0
prefx = [b[0]]
for i in range(1, n):
    c = prefx[i - 1] + b[i]
    prefx.append(c)
maxa = a[n - 1]
for i in range(n - 1):
    maxa = max(a[i], maxa)
    for j in range(i + 1, n):
        ssumi = a[i] + a[j]
        if(j - i == 1):
            if(i >= 1):
                ssumi += max(0, prefx[n - 1] + prefx[i - 1] - prefx[j])
            else:
                ssumi += max(0, prefx[n - 1] - prefx[j])
        else:
            if(i >= 1):
                ssumi += max(prefx[j - 1] - prefx[i], prefx[n - 1] - prefx[j] + prefx[i - 1])
            else:
                ssumi += max(prefx[j - 1] - prefx[i], prefx[n - 1] - prefx[j])
#        print(i,j,ssumi)
        if(ssum < ssumi):
            ssum = ssumi
print(max(ssum, maxa))
