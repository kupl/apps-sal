t = int(input())


def solve(arr):
    if len(arr) == 1:
        return [0, arr]
    ans = 0
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    (val1, lis1) = solve(left)
    (val2, lis2) = solve(right)
    (val, lis) = merge(lis1, lis2)
    return [val + val1 + val2, lis]


def merge(left, right):
    ans = []
    final = 0
    (i, j) = (0, 0)
    n = len(left)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans += [left[i]]
            i += 1
        else:
            ans += [right[j]]
            final += n - i
            j += 1
    ans += left[i:] + right[j:]
    return [final, ans]


for _ in range(t):
    (n, d) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    dic = {i: [] for i in range(d)}
    found = False
    for i in range(n):
        if (arr[i] - i - 1) % d != 0:
            found = True
            break
        elif arr[i] % d == 0:
            dic[0] += [arr[i] // d - 1]
        else:
            dic[arr[i] % d] += [(arr[i] - arr[i] % d) // d]
    if found:
        print(-1)
    else:
        ans = 0
        for perm in list(dic.values()):
            ans += solve(perm)[0]
        print(ans)
