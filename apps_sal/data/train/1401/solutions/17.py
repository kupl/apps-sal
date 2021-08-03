n, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
sum = 0
count = 0
for i in range(len(li)):
    sum = sum + li[i]
    if sum <= k:
        count = count + 1
    else:
        break
print(count)
