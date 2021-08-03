# import Queue
# q = Queue.Queue()
def bfs(visited, musium, count, roads, explore):
    visited[explore - 1] = True
    count[0] += musium[explore]
    for _ in roads[explore]:
        if not visited[_ - 1]:
            bfs(visited, musium, count, roads, _)


t = int(input())
while t > 0:
    n, m, k = list(map(int, input().split()))

    roads = {i: [] for i in range(1, n + 1)}
    visited = [False for _ in range(n)]
    for _ in range(m):
        s, e = list(map(int, input().split()))
        roads[s].append(e)
        roads[e].append(s)
    musium = []
    hashm = {}
    mp = list(map(int, input().split()))
    for i in enumerate(mp, 1):
        musium.append(i)
        hashm.update({i[0]: i[1]})

    musium.sort(key=lambda x: x[1])
    # print(musium)

    count, lavany, end, begin = [0], True, n - 1, 0

    while k > 0:
        if lavany:
            while visited[musium[end][0] - 1] and end > begin:
                end -= 1
            # visited[musium[end][0]] = True
            bfs(visited, hashm, count, roads, musium[end][0])
            end -= 1

        else:
            while visited[musium[begin][0] - 1] and end > begin:
                begin += 1
            bfs(visited, hashm, count, roads, musium[begin][0])
            begin += 1
        k -= 1
        lavany = not lavany
        if all(visited) and k > 0:
            print(-1)
            break
    else:
        print(count[0])
    t -= 1
