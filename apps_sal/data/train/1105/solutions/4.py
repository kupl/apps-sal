t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    if n == 1:
        print(lst[0])
    elif n == 2:
        print(lst[1])
    elif n == 3:
        if lst[0] + lst[1] <= lst[2]:
            print(lst[2])
        else:
            print(lst[0] + lst[1])
    elif n == 4:
        if lst[3] >= lst[1] + lst[0] + lst[2]:
            print(lst[3])
        else:
            if lst[0] == lst[1] == lst[2] == lst[3]:
                print(2 * lst[0])
            else:
                print(lst[3] + max(lst[0], (lst[1] - lst[3] + lst[2])))
