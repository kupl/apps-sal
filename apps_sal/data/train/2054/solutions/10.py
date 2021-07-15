n = int(input())
arr = []
brr = []
for i in range(n-1):
    u,v = list(map(int,input().split()))
    arr.append(u)
    brr.append(v)
color = list(map(int,input().split()))

ans = []
for i in range(n-1):
    if color[arr[i]-1]!=color[brr[i]-1]:
        if ans==[]:
            ans+=[arr[i],brr[i]]
        else:
            if arr[i] in ans and brr[i] in ans:
                print("NO")
                return
            elif arr[i] in ans:
                ans = [arr[i]]
            elif brr[i] in ans:
                ans = [brr[i]]
            else:
                print("NO")
                return
print("YES")
if len(ans)==0:
    ans.append(1)
print(ans[0])
