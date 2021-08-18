s = input().split()
n = int(s[0])
k = int(s[1])
max = k + 1
l = 1
print(l, end=' ')

for i in range(k):
    if i % 2 == 0:
        l += k
    else:
        l -= k
    k -= 1
    print(l, end=' ')

if max < n:
    for i in range(max + 1, n + 1):
        print(i, end=' ')
