t = int(input())
while(t > 0):
    t -= 1
    s, n = map(int, input().split())
    if(s == 1):
        print(1)
        continue
    res = 0
    i = 0
    res = res + s // n
    m = s % n
    if(m == 0):
        print(res)
        continue
    if(m % 2 == 0 or m == 1):
        res = res + 1
    else:
        res = res + 2
    print(res)
