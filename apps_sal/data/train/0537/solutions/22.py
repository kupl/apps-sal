n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
count = 0

for i in range(n) :
    for j in range(i+1, n) :
        if arr[i] - arr[j] <= -1*k :
            count += 1
            
print(count)
