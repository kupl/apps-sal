n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 0

j = 0
for i in range(n) :
    while(j < n) :
        if arr[j] - arr[i] >= k :
            count += n-j
            break
        j += 1
            
print(count)
