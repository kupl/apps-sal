#chef and droof
for u in range(int(input())):
    flag = 0
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(n):
        if lst[i] % 2 == 0:
            flag = 1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
