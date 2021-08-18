n = int(input())
for i in range(n):
    N = int(input())
    lst = list(map(int, input().split()))
    if N == 1:
        print(lst[0])
    elif N == 2:
        print(lst[1])
    elif N == 3:
        print(lst[1] + max(lst[0], (lst[2] - lst[1])))
    else:
        if lst[3] - lst[2] >= lst[1]:
            print(lst[2] + lst[1] + max(lst[0], lst[3] - (lst[1] + lst[2])))
        else:
            print(lst[3] + max(lst[0], lst[1] + lst[2] - lst[3]))
