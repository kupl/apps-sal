t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    flag = 0
    for j in range(n - 2):
        if(l[j] == l[j + 1] == l[j + 2]):
            flag = 1
            break
        else:
            continue
    if(flag == 1):
        print("Yes")
    else:
        print("No")
