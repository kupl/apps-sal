m = 1000000007
p = [(0, input())] + [input().split('->') for i in range(int(input()))]
s = [(10, i) for i in range(10)]
for d, t in p[::-1]:
    a, b = 1, 0
    for q in t:
        x, y = s[int(q)]
        a, b = a * x % m, (b * x + y) % m
    s[int(d)] = a, b
print(s[0][1])
