t = int(input())
for i in range(t):
    n = int(input())
    lst = [int(i) for i in input().split()]
    m = int(input())
    lst1 = [int(i) for i in input().split()]
    c = 0
    for i in lst:
        if i in lst1:
            c += 1
    f = 0
    if c == m:
        for i in range(m - 1):
            if lst.index(lst1[i]) < lst.index(lst1[i + 1]):
                continue
            else:
                f = 1
                break
        if f == 1:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
