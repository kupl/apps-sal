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
        print(lst[0] + lst[2])
    elif n == 4:
        print(max((lst[0] + lst[3]), (lst[1] + lst[2])))
