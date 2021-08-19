# cook your dish here
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mlst = list(map(int, input().split()))
    lst = []
    chef = []
    ass = []
    mlst.sort()
    for i in range(1, n + 1):
        if i not in mlst:
            lst.append(i)
    for j in range(1, len(lst) + 1):
        if(j % 2 != 0):
            # chef.append(lst[j-1])
            print(lst[j - 1], end=' ')
        else:
            ass.append(lst[j - 1])
            # print(lst[j-1],end=' ')
    print()
    print(*ass, sep=' ')
