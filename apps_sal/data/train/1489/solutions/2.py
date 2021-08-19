(n, k) = input().split()
a = [int(i) for i in n]
k = int(k)
i = 0
n = len(a)
while k > 0 and i < n:
    if a[i] != 9:
        a[i] = 9
        k -= 1
    i += 1
print(''.join(map(str, a)))
