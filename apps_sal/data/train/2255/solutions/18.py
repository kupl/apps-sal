n = int(input())
a = list(map(int,input().split()))
preXor = [0]*n
preXor[0] = a[0]
for i in range(1,n):
    preXor[i] = a[i]^preXor[i-1]
even = {}
odd = {}
count = 0
for i in range(n):
    m = preXor[i]
    if (m==0):
        if (i%2==1):
            count += 1
    if (i%2==0):
        if m in even:
            count += even[m]
            even[m] += 1
        else:
            even[m] = 1
    else:
        if m in odd:
            count += odd[m]
            odd[m] += 1
        else:
            odd[m] = 1
print(count)

