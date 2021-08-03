for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    s = lst[0]
    dis = 0
    for i in range(1, len(lst)):
        if s <= 0:
            break
        s = s - 1 + lst[i]
        dis += 1
    print(s + dis)
