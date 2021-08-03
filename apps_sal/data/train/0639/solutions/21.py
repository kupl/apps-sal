for _ in range(int(input())):
    s = input()
    l = []
    for i in set(s):
        l.append(s.count(i))
    l = sorted(l)
    if len(l) < 3 or l[-1] == l[-2] + l[-3]:
        print('Dynamic')
    else:
        print('Not')
