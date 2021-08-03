for i in range(int(input())):
    m = int(input())
    lst = list(map(int, input().split()))
    l = max(lst)
    lst.sort()
    count = 0
    for i in range(m - 1, -1, -2):
        count += lst[i]
    print(count)
