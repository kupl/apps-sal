def solve(A):
    res, pre = set(), {0}
    for x in A:
        pre = {x | y for y in pre} | {x}
        res |= pre
    return len(res)


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if(solve(arr) != n * (n + 1) // 2):
        print('NO')
    else:
        print('YES')
