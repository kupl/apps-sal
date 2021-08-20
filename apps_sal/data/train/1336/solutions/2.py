entry = input()
t = 0
while entry != '0':
    t += 1
    mymap = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    n = list(map(int, entry.split()))
    for i in range(min(n), max(n) + 1):
        for j in str(i):
            mymap[j] += 1
    store1 = list(mymap.items())
    store1.sort()
    print('Case %s: %s' % (t, ' '.join(['%s:%s' % (k, v) for (k, v) in store1])))
    entry = input()
