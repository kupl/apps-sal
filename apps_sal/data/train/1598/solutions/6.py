from operator import itemgetter
t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    d = {}
    sum1 = 0
    for i in range(n):
        (name, p_mobile, marks) = map(str, input().split())
        d['name'] = name
        d['p_mobile'] = p_mobile
        d['marks'] = int(marks)
        l.append(d)
        sum1 += int(marks)
        d = {}
    avg = sum1 / n
    l = sorted(l, key=itemgetter('marks'))
    for i in l:
        if i['marks'] < avg:
            print(i['name'], i['p_mobile'], i['marks'])
