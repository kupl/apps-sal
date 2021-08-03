for _ in range(int(input())):
    n = int(input())
    l = []
    f = 0
    while not l or len(l) < len(l[0]):
        l.append(list(map(int, input().split())))
    a = sum(l, [])
    b = [i for i in range(len(a)) if a[i] == 1]
    for j in range(len(b) - 1):
        if b[j + 1] - b[j] == 1:
            f = 1
            print("UNSAFE")
            break
    if f != 1:
        print("SAFE")
