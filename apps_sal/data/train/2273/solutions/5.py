for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for i in range(n)]
    for i in range(n):
        graph[(i + a[i]) % n].append(i)
        graph[i].append((i + a[i]) % n)
    for v in graph:
        if len(v) != 2:
            print("NO")
            break
    else:
        print("YES")
