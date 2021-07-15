n = int(input())
x =[]
ans ="NO"
arr = list(map(int,input().split()))
arr.sort()

for i in range(n-2):
    if arr[i] + arr[i+1] > arr[i+ 2]:
        ans = "YES"
        x.append(i)
        
print(ans)
if ans == "YES":
    print(arr[max(x)+2], arr[max(x)+1], arr[max(x)])
