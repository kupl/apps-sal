n = int(input().strip())
l = [int(x) for x in input().strip().split()]
p = int(input().strip())
l.sort()
left = 0
right = n - 1
maxo = 0
cur = 0
while left <= right:
    if p >= l[left]:
        p -= l[left]
        left += 1
        cur += 1
        maxo = max(maxo, cur)
    elif cur > 0:
        p += l[right]
        right -= 1
        cur -= 1
    else:
        break
print(maxo)
