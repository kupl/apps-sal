n = int(input())
l = list(map(int, input().split()))
k = int(input())
b = sum(l[:k])
c = 0
i = k - 1
j = n - 1
while i != -1:
    b = b - l[i] + l[j]
    c = max(c, b)
    i -= 1
    j -= 1
print(c)
