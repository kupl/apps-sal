from queue import Queue

n, k = map(int, input().split())
a = [tuple(sorted(list(map(lambda x: int(x) - 1, input().split())))) for i in range(k)]
a = list(set(a))
a.sort()
edges = [[] for i in range(n)]
for i in a:
    edges[i[0]].append(i[1])
    edges[i[1]].append(i[0])

ans = 0
visited = [False for i in range(n)]
queue = Queue(maxsize=n)
for j in range(len(a)):
    if not visited[a[j][0]] and visited[a[j][1]]:
        visited[a[j][0]] = True
        s = a[j][0]
        ans += 1

        queue.put(s)
        while not queue.empty():
            s = queue.get()
            for i in edges[s]:
                if visited[i] == False:
                    queue.put(i)
                    visited[i] = True
                    ans += 1

    elif visited[a[j][0]] and not visited[a[j][1]]:
        visited[a[j][1]] = True
        s = a[j][1]
        ans += 1

        queue.put(s)
        while not queue.empty():
            s = queue.get()
            for i in edges[s]:
                if visited[i] == False:
                    queue.put(i)
                    visited[i] = True
                    ans += 1
    elif not visited[a[j][0]] and not visited[a[j][1]]:
        visited[a[j][0]] = True
        visited[a[j][1]] = True
        ans += 1

        s = a[j][0]
        queue.put(s)
        while not queue.empty():
            s = queue.get()
            for i in edges[s]:
                if visited[i] == False:
                    queue.put(i)
                    visited[i] = True
                    ans += 1

        s = a[j][1]
        queue.put(s)
        while not queue.empty():
            s = queue.get()
            for i in edges[s]:
                if visited[i] == False:
                    queue.put(i)
                    visited[i] = True
                    ans += 1
print(abs(k - ans))
