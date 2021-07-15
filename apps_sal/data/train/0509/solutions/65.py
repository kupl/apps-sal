import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    number = [0] * N
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        u -= 1; v -= 1
        edges[u].append((v, c))
        edges[v].append((u, c))

    # import
    from collections import deque
    
    # BFS for tree
    # please prefer those objects
    # ki: adjacency list
    # N: length of vertex list
    fr = 0
    que = deque([fr])
    number[fr] = 1
    for _ in range(N**2):
        fr = que.popleft()
        for to, c in edges[fr]:
            if number[to] == 0:
                que.append(to)
                if number[fr] != c:
                    number[to] = c
                else:
                    if c == 1:
                        number[to] = 2
                    else:
                        number[to] = 1
        if len(que) == 0:
            break

    print(*number, sep = '\n')

def __starting_point():
    main()

__starting_point()
