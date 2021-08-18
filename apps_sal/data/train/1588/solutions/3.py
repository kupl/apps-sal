def comp(a, b):
    if len(a) > len(b):
        return b
    elif len(b) > len(a):
        return a
    else:
        i = 0
        while True:
            if a[i] > b[i]:
                return b
            else:
                return a
            i += 1


for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(n):
        name, score = map(str, input().split())
        a.append([name, score])
        if score not in c:
            if score in b:
                b.remove(score)
                c.append(score)
            else:
                b.append(score)

    if len(b) == 0:
        print("Nobody wins.")
    else:
        ans = b[0]
        for i in range(1, len(b)):
            ans = comp(ans, b[i])
        for i in range(len(a)):
            if a[i][1] == ans:
                print(a[i][0])
