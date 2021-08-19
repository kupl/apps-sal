"""
Created on Sun Jan 24 09:23:33 2021

@author: gourob
"""
test = int(input())
while test:
    flag = 1
    n = int(input())
    elem = list(map(int, input().split()))
    (p1, p2) = (0, n - 1)
    if elem[0] != 1:
        flag = 0
    else:
        while p1 < p2:
            if elem[p1] != elem[p2]:
                flag = 0
                break
            if not (elem[p1] == elem[p1 + 1] or elem[p1] + 1 == elem[p1 + 1]):
                flag = 0
                break
            if elem[p1] > 7:
                flag = 0
                break
            p1 += 1
            p2 -= 1
    if elem[p1] != 7:
        flag = 0
    if flag == 1:
        print('yes')
    else:
        print('no')
    test -= 1
