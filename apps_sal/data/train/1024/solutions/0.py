# cook your dish here
extra, less = 0, 0
for _ in range(int(input())):
    sli, mem, sma, luc = list(map(int, input().split()))
    total = sma
    t = sma
    while mem > 1:
        t *= luc
        total += t
        mem -= 1
    if total <= sli:
        extra += sli - total
        print('POSSIBLE', sli - total)
    else:
        less += total - sli
        print('IMPOSSIBLE', total - sli)
if extra >= less:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
