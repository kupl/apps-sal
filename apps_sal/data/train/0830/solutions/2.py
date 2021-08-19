from collections import deque
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = input()
    b = input()
    amap = {}
    bmap = {}
    for (i, char) in enumerate(a):
        if char in amap:
            amap[char].append(i)
        else:
            amap[char] = [i]
    for (i, char) in enumerate(b):
        if char in bmap:
            bmap[char].append(i)
        else:
            bmap[char] = [i]
    ans = []
    flag = False
    for letter in range(25, -1, -1):
        char = chr(ord('a') + letter)
        if char in bmap:
            if char not in amap:
                flag = True
                break
            else:
                ans.append([])
                for ind in bmap[char]:
                    if a[ind] < char:
                        flag = True
                        break
                    elif a[ind] == char:
                        pass
                    else:
                        ans[-1].append(ind)
                if len(ans[-1]):
                    ans[-1].append(amap[char][0])
                else:
                    ans.pop()
        if flag:
            break
    if flag:
        print(-1)
    else:
        print(len(ans))
        for item in ans:
            print(len(item), end=' ')
            print(*item)
