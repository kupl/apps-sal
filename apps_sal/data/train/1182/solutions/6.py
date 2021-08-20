t = int(input())
m = [int(input()) for i in range(t)]
for i in m:
    c = 0
    ANS = []
    if i % 2 != 0:
        for a1 in range(i + 1, 2 * i + 1, 2):
            intp = a1 * i / (a1 - i)
            if intp >= a1 and a1 * i % (a1 - i) == 0:
                c = c + 1
                ANS.append(a1)
    else:
        for a1 in range(i + 1, 2 * i + 1, 1):
            intp = a1 * i / (a1 - i)
            if intp >= a1 and a1 * i % (a1 - i) == 0:
                c = c + 1
                ANS.append(a1)
    ANS.sort()
    print(c)
    for j in ANS:
        print(j)
