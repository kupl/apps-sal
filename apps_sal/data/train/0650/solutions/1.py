def solve(array):
    L = len(array)
    if L <= 1:
        return L
    array.sort()
    cnt = 1
    for i in range(1, L):
        if array[i][1] * -1 >= array[i - 1][0]:
            cnt += 1
    return cnt


for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    rooms = [[] for i in range(K)]
    for i in range(N):
        s, e, p = list(map(int, input().split()))
        rooms[p - 1].append([e, -s])

    ans = 0
    for i in rooms:
        ans += solve(i)
    print(ans)
