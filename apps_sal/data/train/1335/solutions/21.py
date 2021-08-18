n = int(input())
lis = list(map(int, input().split()))[:n]
arr = list(set(lis))
sum_ = 0
for i in range(len(arr)):
    sum_ += (lis.count(arr[i]) // 2) + (lis.count(arr[i]) % 2)
print(sum_)
