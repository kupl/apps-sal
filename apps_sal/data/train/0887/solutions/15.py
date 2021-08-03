t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a[0] != 0 or b[n - 1] != 0 or a[n - 1] != b[0] or b[0] == 0:
        print("No")
    else:
        flag = 0
        for i in range(n):
            if (a[i] + b[i] < b[0] or a[i] + b[0] < b[i] or b[i] + b[0] < a[i]):
                flag = 1
                break
        if flag == 1:
            print("No")
        else:
            print("Yes")
