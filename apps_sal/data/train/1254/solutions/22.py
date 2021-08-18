for t in range(int(input())):
    n, p = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    count = 0
    cout = 0
    for j in ls:
        if j <= (p // 10):
            count += 1
        if j >= (p // 2):
            cout += 1
    if (count == 2 and cout == 1):
        print("yes")
    else:
        print("no")
