# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    m = int(input())
    l1 = [int(i) for i in input().split()]
    c = 0
    f = 0
    for i in l1:
        if i in l:
            c = c + 1
    if c == len(l1):
        for i in range(m - 1):
            if l.index(l1[i]) < l.index(l1[i + 1]):
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
