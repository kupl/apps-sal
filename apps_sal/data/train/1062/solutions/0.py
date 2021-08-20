def read_i_l(l=False):
    m = list(map(int, input().strip().split(' ')))
    if l:
        return list(m)
    else:
        return m


def i():
    return int(input().strip())


T = i()
L = []
'for current in range(T):\n    line = ""\n    for i in range(current):\n        line+=str((T-i)%10)\n    for i in range(2*(T-current)-1):\n        line+=str((T-current)%10)\n    for i in range(current-1,-1,-1):\n        line+=str((T-i)%10)\n    L.append(line)\nL += L[-2::-1]'
if T >= 1:
    L = ['1']
for i in range(2, T + 1):
    nL = [str(i) + (2 * i - 2) * (' ' + str(i))]
    for l in L:
        nL.append(str(i) + ' ' + l + ' ' + str(i))
    nL.append(str(i) + (2 * i - 2) * (' ' + str(i)))
    L = nL
for l in L:
    print(l)
