for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l1 = [0] * k
    l2 = [1] * k
    ans, temp = 0, 0

    for i in l:
        l1[i - 1] = 1
        temp += 1
        if l1 == l2:
            ans = max(ans, (temp - 1))
            l1 = [0] * k
            l1[i - 1] = 1
            temp = 1

    print(max(ans, temp))
