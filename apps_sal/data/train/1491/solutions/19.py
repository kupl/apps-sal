li = list(map(int, input().split()))
li = sorted(li)
(a, b, c, d) = li
if float(b / float(a)) == float(d / float(c)):
    print('Possible')
else:
    print('Impossible')
