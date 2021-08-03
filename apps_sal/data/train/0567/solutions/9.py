for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 2):
        if(a[i] == a[i + 1] and a[i] == a[i + 2]):
            ans = 1
    if ans == 1:
        print('Yes')
    else:
        print('No')
