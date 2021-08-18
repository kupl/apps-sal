for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    flag = 0
    l2 = []
    for i in range(len(l1)):
        if l1[i] == 1:
            l2.append(i)
    for i in range(len(l2) - 1):
        if l2[i + 1] - l2[i] < 6:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
