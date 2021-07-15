for _ in range(int(input())):
    n,k = [int(c) for c in input().split()]
    a = [int(c) for c in input().split()]
    ls = a
    if n==1:
        print("YES")
        print(1)
        continue
    if k==1:
        print("NO")
        continue
    
    if k==2 and n>2:
        if ls[0]!=ls[1]-1:
            print("NO")
            continue

    ans = [0 for i in range(n+1)]
    count = n
    for i in range(1,a[1]):
        if i != a[0]:
            ans[i]  =count
            count-=1
    for i in a[::-1]:
        ans[i] = count
        count-=1
    for i in range(1,n+1):
        if ans[i] == 0:
            ans[i] = count
            count-=1
    print("YES")
    print(*ans[1:])
