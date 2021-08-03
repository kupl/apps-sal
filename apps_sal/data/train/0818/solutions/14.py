t = int(input())
for test in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    check = [0 for i in range(n + 2)]
    for i in range(n):
        check[i + 1] = check[i]
        if(arr[i] % 2 == 0):
            check[i + 1] += 1
    q = int(input())
    for i in range(q):
        l, r = list(map(int, input().split()))
        if(check[r] - check[l - 1]) > 0:
            print("EVEN")
        else:
            print("ODD")
