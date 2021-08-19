(n, q) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
xor = a[0]
for i in range(1, len(a)):
    xor = xor ^ a[i]
a.append(xor)
s = [a[0]]
for i in range(1, len(a)):
    s.append(s[-1] ^ a[i])
for I in range(q):
    k = int(input())
    k -= 1
    print(s[k % (n + 1)])
