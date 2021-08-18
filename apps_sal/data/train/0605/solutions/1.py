a = int(input())
for i in range(a):
    b = list(map(int, str(input()).split(' ')))
    c = str(input())
    li1 = [0]
    li2 = [0]
    for i1 in range(len(c)):
        if c[i1] == 'R':
            li1.append(li1[len(li1) - 1] + 1)
        elif c[i1] == 'L':
            li1.append(li1[len(li1) - 1] - 1)
        elif c[i1] == 'U':
            li2.append(li2[len(li2) - 1] + 1)
        else:
            li2.append(li2[len(li2) - 1] - 1)
    if (max(li1) - min(li1) + 1) <= b[1] and (max(li2) - min(li2) + 1) <= b[0]:
        print('safe')
    else:
        print('unsafe')
