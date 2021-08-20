import sys
alpha = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(sys.stdin.readline())):
    n1 = sys.stdin.readline().strip().lower().replace(' ', '')
    n2 = sys.stdin.readline().strip().lower().replace(' ', '')
    common = [0 for i in range(26)]
    for i in range(26):
        t1 = n1.count(alpha[i])
        t2 = n2.count(alpha[i])
        if t1 == t2:
            common[i] = t1
        else:
            common[i] = min([t1, t2])
    for a in range(26):
        n1 = n1.replace(alpha[a], '', common[a])
        n2 = n2.replace(alpha[a], '', common[a])
    remain = len(n1) + len(n2)
    f = ['f', 'l', 'a', 'm', 'e', 's']
    index = 0
    while len(f) > 1 and remain != 0:
        l = remain % len(f) - 1
        del f[l]
        if l != 0 and l != -1:
            f = f[l:] + f[:l]
    if f[0] == 'f' and remain != 0:
        print('FRIENDS')
    elif f[0] == 'l':
        print('LOVE')
    elif f[0] == 'a':
        print('ADORE')
    elif f[0] == 'm':
        print('MARRIAGE')
    elif f[0] == 'e':
        print('ENEMIES')
    elif f[0] == 's':
        print('SISTER')
    elif remain == 0:
        print('SISTER')
