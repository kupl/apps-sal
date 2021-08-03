t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    search = 0
    for i in range(len(a)):
        if(a[i] >= k):
            search = 1
            break
    if(search == 1):
        print("YES")
    else:
        print("NO")
