(n, d) = input().split(' ')
n = int(n)
d = int(d)
queue = [int(i) for i in input().split()]
ans = 0


def find_max(begin, start, end):
    while start < end:
        mid = (start + end) // 2
        if queue[mid] - queue[begin] <= d:
            start = mid + 1
        else:
            end = mid
    mid = (start + end) // 2
    if queue[mid] - queue[begin] > d:
        mid -= 1
    return mid


for i in range(n - 2):
    if i == 0:
        j = find_max(i, i + 2, n - 1)
    else:
        j = find_max(i, j, n - 1)
    if j - i < 2:
        continue
    else:
        ans += (j - i) * (j - i - 1) // 2
print(ans)
