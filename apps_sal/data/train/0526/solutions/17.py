from collections import Counter
for _ in range(int(input())):
    S = list(map(str, input()))
    original = 8
    new = 8
    if S[0].isdigit():
        original = 32
        new = 32
    a = S[0]
    b = 0
    for i in range(1, len(S)):
        if S[i].isdigit():
            original += 32
            new += 32
        else:
            original += 8
            if S[i] == a:
                b = 32
            else:
                new += b + 8
                b = 0
        a = S[i]
    new += b
    print(original - new)
