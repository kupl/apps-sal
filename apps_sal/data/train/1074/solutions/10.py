t = int(input())
for i in range(t):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = []
    for j in lst1:
        if j not in lst2:
            lst2.append(j)
    lst3 = []
    for k in lst2:
        lst3.append(lst1.count(k))
    c1 = 0
    for j in lst3:
        c = j
        if c >= 2:
            while(c >= 2):
                c1 += 1
                c = c - 2
    print(round(c1 / 2))
# cook your dish here
