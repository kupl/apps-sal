# cook your dish here
n, q = list(map(int, input().split()))

a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(n):
    if i == 0:
        s[i] = a[i]
    else:
        s[i] = s[i - 1] ^ a[i]
s[n] = 0
for _ in range(q):
    k = int(input())
    k -= 1
    k = k % (n + 1)
    print(s[k])
