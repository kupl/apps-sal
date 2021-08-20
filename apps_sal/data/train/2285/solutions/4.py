import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))


t = int(input())
for tt in range(t):
    n = int(input())
    d_str = input()
    d = []
    for i in range(n):
        d.append(int(d_str[i]))
    di = []
    for i in range(n):
        di.append(i)
    for b in range(10):
        one_min = -1
        two_min = -1
        not_ok = 0
        ans = []
        for i in range(n):
            if d[i] < b:
                if d[i] < one_min:
                    not_ok = 1
                    break
                one_min = d[i]
                ans.append(1)
            elif d[i] > b:
                if d[i] < two_min:
                    not_ok = 1
                    break
                two_min = d[i]
                ans.append(2)
            elif b >= two_min:
                two_min = b
                ans.append(2)
            elif b >= one_min:
                one_min = b
                ans.append(1)
            else:
                not_ok = 1
                break
        if not_ok != 1:
            print(''.join(map(str, ans)))
            break
    else:
        print('-')
