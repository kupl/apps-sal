t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    m = []
    for i in range(n):
        if l[i] == 1:
            m.append(i)
    if len(m) == 1:
        print("YES")
    else:
        diff = []
        for i in range(1, len(m)):
            diff.append(m[i] - m[i - 1])
        for i in diff:
            if i < 6:
                print("NO")
                break
        else:
            print("YES")
    t -= 1
