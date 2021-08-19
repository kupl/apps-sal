from collections import Counter
for _ in range(int(input())):
    S = list(map(str, input()))
    original = 8
    new = 0
    if S[0].isdigit():
        original = 32
    lst = [S[0]]
    lst1 = [1]
    b = 0
    for i in range(1, len(S)):
        if S[i].isdigit():
            original += 32
        else:
            original += 8
        if S[i] == lst[-1]:
            lst1[-1] += 1
        else:
            lst.append(S[i])
            lst1.append(1)
    for i in range(len(lst)):
        if lst[i].isdigit():
            if lst1[i] > 1:
                new += 64
            else:
                new += 32
        elif lst1[i] > 1:
            new += 40
        else:
            new += 8
    print(original - new)
