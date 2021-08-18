n, k = list(map(int, input().split()))
n = str(n)
l = list(n)
n = len(l)
for i in range(n):
    if(k > 0):
        if(l[i] != '9'):
            l[i] = '9'
            k -= 1
print(''.join(l))
