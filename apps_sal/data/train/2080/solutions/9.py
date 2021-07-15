m = int(input())
q = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
q.sort()

ans = 0
mm = q[0]

i = 0
while i<n:
    j = i
    if j+mm <= n:
        while i < j+mm:
            ans+=a[i]
            i+=1
        i+=1
    else:
        break
    i+=1
if i <n:
    ans += sum(a[i:])
print(ans)
    

