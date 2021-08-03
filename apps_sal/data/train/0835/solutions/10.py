for i in range(eval(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 1 and a[1] == 2:
        print("Yes")
    elif a[0] == 1 and a[1] % 2 == 0:
        print("No")
    elif a[0] != 1 and a[1] % 2 == 0:
        print("Yes")
    elif (a[0] % 2 == 0 and a[1] % 2 != 0) or (a[1] % 2 == 0 and a[0] % 2 != 0):
        print("Yes")
    else:
        print("No")
