n = int(input())
names = dict()
for i in range(n):
    s = input()
    tp = []
    ks = 0
    l = len(s)
    tp = []
    flag = 0
    for i in range(l):
        if s[i] == 'k':
            ks += 1
            flag = 1
        else:
            if s[i] == 'h' and flag == 1:
                tp.append('h')
            else:
                tp.append('k' * ks)
                if s[i] == 'u':
                    tp.append('oo')
                else:
                    tp.append(s[i])
            ks = 0
            flag = 0
    if ks:
        tp.append('k' * ks)
    s = "".join(tp)
    if s not in list(names.keys()):
        names[s] = 1
print(len(names))
