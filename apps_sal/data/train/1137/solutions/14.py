test = int(input())
ANS = list()
for i in range(test):
    n = int(input())
    items = sorted(list(map(int, input().split())))
    c = 1
    for j in range(len(items)):
        if items[j] < 2000:
            t = 2000 - items[j]
            if t in items[j + 1:]:
                ANS.append("Accepted")
                c = 2
                break
            else:
                pass
        else:
            break
    if c == 1:
        ANS.append("Rejected")
for ans in ANS:
    print(ans)
