# cook your dish here
a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    l = list(map(int, input().split()))
    if len(l) == b:
        d = 0
        for r in l:
            r = r + c
            if r % 7 == 0:
                d += 1
        print(d)
    else:
        print('WARNING')
