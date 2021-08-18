import bisect


def solve(arr, n, ans):
    indices = {}
    dist_vals = []
    for i in range(n):
        if arr[i] not in list(indices.keys()):
            indices[arr[i]] = []
            dist_vals.append(arr[i])

        indices[arr[i]].append(i)

    dist_vals.sort()
    m = 1
    index = -1
    i = 0
    while i < len(dist_vals):
        x = dist_vals[i]
        index = bisect.bisect(indices[x], index)
        if index == len(indices[x]):
            m += 1
            index = -1
        else:
            index = indices[x][index]
            i += 1

    ans.append(m)


def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n, ans)

    for i in ans:
        print(i)


main()
