t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    dict1 = dict()
    dict2 = dict()
    for i in range(n):
        (w, s1) = input().split()
        s = 0
        s = int(s1)
        if s == 0:
            if w not in dict2:
                dict2[w] = 1
            elif w in dict2:
                dict2[w] += 1
        if s == 1:
            if w not in dict1:
                dict1[w] = 1
            elif w in dict1:
                dict1[w] += 1
    for i in dict1:
        if i not in dict2:
            c += dict1[i]
        elif i in dict2:
            c += max(dict1[i], dict2[i])
    for i in dict2:
        if i not in dict1:
            c += dict2[i]
    print(c)
