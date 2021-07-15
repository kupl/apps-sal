t = int(input())
while t > 0:
    n = input().strip()
    f = n.count('4')
    s = n.count('7')
    print(len(n) - (f + s))
    t = t - 1
