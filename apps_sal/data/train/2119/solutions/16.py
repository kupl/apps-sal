n = int(input())
arr = [int(i) for i in input().split()]
des = [int(i) for i in input().split()]
ans = 0
left = [-1 for i in range(n)]
right = [-1 for i in range(n)]
last = 0
presum = []
parr = []
for i in arr:
    presum.append(last + i)
    last += i
for i in des[::-1]:
    l = 0
    r = 0
    parr.append(ans)
    if i == 1 or left[i - 2] == -1:
        left[i - 1] = i - 1
    else:
        left[i - 1] = left[i - 2]
    l = left[i - 1]
    if i == n or right[i] == -1:
        right[i - 1] = i - 1
    else:
        right[i - 1] = right[i]
    r = right[i - 1]
    if l == 0 and ans < presum[r]:
        ans = presum[r]
    elif ans < presum[r] - presum[l - 1]:
        ans = presum[r] - presum[l - 1]
    left[r] = l
    right[l] = r
for i in parr[::-1]:
    print(i)
