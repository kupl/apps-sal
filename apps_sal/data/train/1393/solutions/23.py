for T in range(int(input())):
    n = int(input())
    li = (list(map(int, input().split())))[:n]
    cnt = 1
    for i in range(1, n):
        if li[i] - li[i - 1] < 0:
            cnt += 1
        else:
            li[i] = li[i - 1]
    print(cnt)
