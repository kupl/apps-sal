t = 0
try:
    t = int(input())
except:
    pass
for _ in range(t):
    a, b, c = map(int, input().split())
    d = c % a
    if(d < b):
        print(c - d + b - a)
    else:
        print(c - d + b)
