"""
Created on Sat Oct  3 14:08:49 2020

@author: Vineet
"""
try:

    n, m, k = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        list1 = list(map(int, input().split()[:k + 1]))
        Sum = sum(list1[:k])

        if Sum >= m and list1[-1] <= 10:
            count += 1
        else:
            continue
    print(count)


except:
    pass
