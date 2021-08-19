t = list(input())
p = list(input())


def has_sub(temp):
    idx = 0
    for c in temp:
        if c == p[idx]:
            idx += 1
        if idx == len(p):
            return True
    return False


arr = list(map(int, input().split()))
left = 0
right = len(arr) - 1
while left < right:
    mid = (left + right + 1) // 2
    temp = t[:]
    for idx in range(mid):
        temp[arr[idx] - 1] = '0'
    if has_sub(temp):
        left = mid
    else:
        right = mid - 1
print(right)
