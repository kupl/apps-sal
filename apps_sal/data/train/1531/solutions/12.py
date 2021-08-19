n = int(input())
arr = list(map(int, input().split(' ')))
m = int(input())
for _ in range(m):
    (branch, ind_from_left) = map(int, input().split(' '))
    if branch > 1 and ind_from_left != 1:
        arr[branch - 2] += ind_from_left - 1
    if branch < n and ind_from_left != arr[branch - 1]:
        arr[branch] += arr[branch - 1] - ind_from_left
    arr[branch - 1] = 0
for b in arr:
    print(b)
