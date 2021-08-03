t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    flag = True
    for i in l:
        if i % 2 == 0:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
