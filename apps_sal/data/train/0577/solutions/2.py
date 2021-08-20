import collections


def alphabet():
    s = input()
    d = collections.defaultdict(lambda: 0)
    for i in s:
        d[i] += 1
    n = int(input())
    for i in range(n):
        w = input()
        flag = True
        for i in w:
            if i not in d:
                print('No')
                flag = False
                break
        if flag:
            print('Yes')


alphabet()
