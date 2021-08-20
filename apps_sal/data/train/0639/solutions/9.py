from itertools import permutations
for _ in range(int(input())):
    st = input()
    s = set(st)
    l = []
    for i in set(s):
        l.append(st.count(i))
    l.sort()
    if len(l) < 3 or l[-1] == l[-2] + l[-3]:
        print('Dynamic')
    else:
        print('Not')
