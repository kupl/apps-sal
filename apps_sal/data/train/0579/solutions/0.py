t=int(input())
def check():
    pref = [0]*n
    pref[0]=a[0]
    suff = [0]*n
    suff[-1]=a[-1]
    for i in range (1,n):
        pref[i] = pref[i-1]|a[i]
        suff[n-i-1] = suff[n-i]|a[n-i-1]
    if suff[1]==k:
        return 0
    elif pref[n-2]==k:
        return n-1
    else:
        for i in range (1,n-1):
            if pref[i-1]|suff[i+1] == k:
                return i
        return -1
while(t):
    t-=1
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    ans = []
    arr = [0]*n
    for i in range (n):
        if k|a[i] != k:
            a[i] = a[i-1]|a[(i+1)%(n)]
            ans.append(i+1)
            arr[i]=1

    x = 0
    count = 0
    for i in range (n):
        x|=a[i]
        
    if x!= k:
        print(-1)
    else:
        y = check()
        if y == -1:
            print(-1)
        else:
            for i in range (y,n+y):
                if arr[i%n]==0:
                    arr[i%n]==1
                    ans.append((i%n)+1)
            print(*ans)
