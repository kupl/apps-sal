for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    fl = 1
    if(a[0] != 0 or b[n - 1] != 0 or a[n - 1] != b[0]):
        fl = 0
    s = b[0]
    if(fl):
        for i in range(n):
            if(i != 0 and i != n - 1):
                if(a[i] == 0 or b[i] == 0):
                    fl = 0
                    break

            if(a[i] + b[i] < s):
                fl = 0
                break
            if(s + b[i] < a[i]):
                fl = 0
                break
            if(s + a[i] < b[i]):
                fl = 0
                break
    if(fl):
        print("Yes")
    else:
        print("No")
