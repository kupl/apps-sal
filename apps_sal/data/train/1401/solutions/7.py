t, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
c = 0
sum1 = 0
for i in arr:
    sum1 += i
    if sum1 > k:
        break
    elif sum1 == k:
        c += 1
        break
    c += 1
print(c)
