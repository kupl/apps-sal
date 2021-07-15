
n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
new = []
check = 0
for i in range(2,n):
    if (arr[i-2] + arr[i-1]) > arr[i]:
        new.append((arr[i-2],arr[i-1],arr[i]))
if len(new) == 0:
    print("NO")
else:
    print("YES")
    ans = max(new)
    print(" ".join([str(i) for i in reversed(ans)]))

