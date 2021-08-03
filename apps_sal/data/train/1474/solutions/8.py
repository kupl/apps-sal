for tc in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))
    k = input()
    cur = -1
    tmp = -2
    for i in a:
        if k in i:
            if i.count(k) > cur:
                cur = i.count(k)
                tmp = i
    print(tmp)
