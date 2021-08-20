"""
Created on Tue Nov  5 17:14:44 2019

@author: hkumar50
"""
'\nCreated on Tue Nov  5 15:53:29 2019\n\n@author: hkumar50\n'


def calres(x):
    l = len(x)
    x = list(x)
    flag = 0
    if l % 2 != 0:
        totItr = l // 2 + 1
    else:
        totItr = l // 2
    for i in range(0, totItr):
        if x[i] == '.' or x[l - 1 - i] == '.':
            if len(x) % 2 != 0 and (i == len(x) // 2) == l - 1 - i:
                x[i] = 'a'
            elif x[i] == '.' and x[l - 1 - i] != '.':
                x[i] = x[l - 1 - i]
            elif x[i] != '.' and x[l - 1 - i] == '.':
                x[l - 1 - i] = x[i]
            elif x[i] == '.' and x[l - 1 - i] == '.':
                x[i] = 'a'
                x[l - 1 - i] = 'a'
        elif x[i] == x[l - 1 - i]:
            flag = 1
        else:
            flag = -1
            break
    if flag == -1:
        print('-1')
    else:
        print(''.join(x))


t = int(input())
for i in range(t):
    val = str(input())
    calres(val)
