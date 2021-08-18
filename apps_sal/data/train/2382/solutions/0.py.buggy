def isvalid(s):
    nonlocal l
    for i in l:
        count = 0
        for j in range(len(i)):
            if(s[j] != i[j]):
                count += 1
        if(count > 1):
            return 0
    return 1


t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    m = int(l[1])
    l = []
    for i in range(n):
        s = input()
        l.append(s)
    poss = 0
    ans = 0
    for i in range(m):
        copy = [x for x in l[0]]
        for j in range(26):
            copy[i] = chr(97 + j)
            if(isvalid(copy)):
                poss = 1
                ans = copy
                break
        if(poss == 1):
            break
    if(poss):
        for i in ans:
            print(i, end="")
        print()
    else:
        print(-1)
