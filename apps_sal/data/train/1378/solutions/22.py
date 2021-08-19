# cook your dish here
a, n, k = map(int, input().split())

res = [0] * k

for i in range(k):
    res[i] = ((a // ((n + 1)**i)) % (n + 1))

print(' '.join(str(i) for i in res))
