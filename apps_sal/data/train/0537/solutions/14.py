n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
i = 0
res = 0
while(i < len(arr)):
    j = i + 1
    while(j < len(arr)):
        if(arr[j] - arr[i] >= k):
            res = res + len(arr) - j
            break
        j += 1
    i += 1
print(res)
