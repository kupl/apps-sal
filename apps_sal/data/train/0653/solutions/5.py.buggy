n = int(input())
arr = list(map(int, input().split()))
h = int(input())
arr.sort()
ans = 0
i = 0
if n == 1 and h >= arr[0]:
    print(1)
    return
while(len(arr) != 0):
    if arr[i] > h and len(arr) > 1:
        h += arr[-1]
        ans -= 1
        del arr[-1]
    elif len(arr) == 1:
        break
    h -= arr[i]
    del arr[i]
    ans += 1
print(max(ans, 0))
