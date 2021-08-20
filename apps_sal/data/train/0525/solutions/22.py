t = int(input())
for i in range(t):
    lst = input().split()
    for j in range(3):
        lst[j] = int(lst[j])
    if lst[2] % lst[0] == lst[1]:
        print(lst[2])
    elif lst[2] % lst[0] < lst[1]:
        print(lst[2] - (lst[0] - lst[1] + lst[2] % lst[0]))
    else:
        print(lst[2] - (lst[2] % lst[0] - lst[1]))
