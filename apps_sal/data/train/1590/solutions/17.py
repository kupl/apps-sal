for _ in range(int(input())):
    l = sorted(list(map(int, input().split())))
    if l[0] + l[1] + 1 >= l[2]:
        print("Yes")
    else:
        print("No")
