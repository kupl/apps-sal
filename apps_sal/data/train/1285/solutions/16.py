for t in range(int(input())):
    l = int(input())
    m = []
    for r in range(l):
        m.append(list(map(int, input().split())))
    maxsum = 0
    for i in range(l):
        s1 = 0
        s2 = 0
        for j in range(i + 1):
            s1 += m[j][l + j - i - 1]
            s2 += m[l + j - i - 1][j]
        if maxsum < s1:
            maxsum = s1
        if maxsum < s2:
            maxsum = s2

    print(maxsum)
