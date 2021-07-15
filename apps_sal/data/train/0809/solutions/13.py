n = int(input())
j =""
ans ="NO"
arr = list(map(int,input().split()))
arr.sort()

for i in range(n-2):
    if arr[i] + arr[i+1] > arr[i+ 2]:
        ans = "YES"
        j = i
        
print(ans)
if ans == "YES":
    print(arr[j+2], arr[j+1], arr[j])
