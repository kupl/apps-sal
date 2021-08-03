from itertools import permutations as p


def disc(a, b):
    for ai in a:
        for bi in b:
            if ai == bi:
                return False
    return True


for i in range(eval(input())):
    n = eval(input())
    arr = list(map(int, input().split()))
    perms = list(p(arr))
    m = eval(input())
    offer = {}
    for i in range(m):
        dup = list(map(int, input().split()))
        try:
            offer[dup[0]].append(dup[1:])
        except:
            offer[dup[0]] = [dup[1:]]
    ans = sum(arr)
    if n == 1:
        print(ans)
    elif n == 2:
        try:
            if len(offer[2]) >= 1:
                ans -= min(arr)
        except:
            pass
        print(ans)
    elif n == 3:
        try:
            if len(offer[3]) >= 1:
                ans -= min(arr)
        except:
            pass
        try:
            if len(offer[2]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur += item[0]
                    cur += max(item[1], item[2])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
        except:
            pass
        print(ans)
    elif n == 4:
        try:
            if len(offer[4]) >= 1:
                ans -= min(arr)
        except:
            pass
        # print ans
        try:
            if len(offer[3]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur = sum(item)
                    cur -= min(item[1], item[2], item[3])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
        except:
            pass
        # print ans
        try:
            if len(offer[2]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur = sum(item)
                    cur -= min(item[1], item[2])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
                # print ans
            # print offer[2]
            if len(offer[2]) >= 2:
                flg = False
                end = len(offer[2])
                for i in range(end):
                    for j in range(i + 1, end):
                        if disc(offer[2][i], offer[2][j]):
                            flg = True
                            break
                # print flg
                if flg:
                    value = 9999999999
                    for item in perms:
                        cur = 0
                        cur = sum(item)
                        cur -= min(item[1], item[0])
                        cur -= min(item[2], item[3])
                        if cur < value:
                            value = cur
                    if value < ans:
                        ans = value
        except:
            pass
        print(ans)
    elif n == 5:
        try:
            if len(offer[5]) >= 1:
                ans -= min(arr)
        except:
            pass
        try:
            if len(offer[4]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur = sum(item)
                    cur -= min(item[1], item[2], item[3], item[4])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
        except:
            pass
        try:
            if len(offer[2]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur = sum(item)
                    cur -= min(item[1], item[2])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
            if len(offer[2]) >= 2:
                flg = False
                end = len(offer[2])
                for i in range(end):
                    for j in range(i + 1, end):
                        if disc(offer[2][i], offer[2][j]):
                            flg = True
                            break
                if flg:
                    value = 9999999999
                    for item in perms:
                        cur = 0
                        cur = sum(item)
                        cur -= min(item[1], item[0])
                        cur -= min(item[2], item[3])
                        if cur < value:
                            value = cur
                    if value < ans:
                        ans = value
        except:
            pass
        try:
            if len(offer[3]) >= 1:
                value = 9999999999
                for item in perms:
                    cur = 0
                    cur = sum(item)
                    cur -= min(item[1], item[2], item[3])
                    if cur < value:
                        value = cur
                if value < ans:
                    ans = value
        except:
            pass
        try:
            if len(offer[3]) >= 1 and len(offer[2]) >= 1:
                flg = False
                for i in offer[3]:
                    for j in offer[2]:
                        if disc(i, j):
                            flg = True
                            break
                if flg:
                    value = 9999999999
                    for item in perms:
                        cur = 0
                        cur = sum(item)
                        cur -= min(item[1], item[0])
                        cur -= min(item[2], item[3], item[4])
                        if cur < value:
                            value = cur
                    if value < ans:
                        ans = value
        except:
            pass
        print(ans)
