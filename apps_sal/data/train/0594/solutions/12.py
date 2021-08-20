(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
(inc, enc) = (0, 0)
for i in range(0, len(l)):
    inc = max(l[i], inc + l[i])
    enc = max(enc, inc)
result = sum(l) - enc
print(result + enc / m)
