import sys
n = int(sys.stdin.readline())
res = 0
for i in range(n):
    s = sys.stdin.readline().split()[-1]
    l = len(s)
    a = sum(1 for c in s if c == '8')
    b = sum(1 for c in s if c == '5')
    c = sum(1 for c in s if c == '3')
    if a >= b >= c and a + b + c == l:
        res += 1
print(res)
