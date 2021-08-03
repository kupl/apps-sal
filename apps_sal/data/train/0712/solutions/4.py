# cook your dish here
for _ in range(0, int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    cnt = 0
    for i in range(0, n):
        if(l[i] % 2 == 0):
            cnt += 1
            print("NO")
            break
    if(cnt == 0):
        print("YES")
