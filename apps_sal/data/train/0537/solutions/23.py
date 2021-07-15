n, k = map(int, input().split())
arr = []

arr = list(map(int, input().split()))
count = 0

for i in arr :
    for j in arr :
        if i - j >= k :
            count += 1
            
print(count)
