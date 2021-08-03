# cook your dish here
a, n, k = map(int, input().split())
b = [0] * k
i = 0
while(i < k):
    b[i] = a % (n + 1)
    a = a // (n + 1)
    i += 1
print(*b, sep=' ')
