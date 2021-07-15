from collections import deque
def main():
    n,m = map(int,input().split())
    G = dict()
    for i in range(1,n+1):
        G[i] = dict()

    for i in range(m):
        u,v,c = map(int,input().split())
        G[u][v] = c
        G[v][u] = c

    done = [0]*(n+1)
    done[1] = 1

    dq = deque()
    dq.append(1)

    while dq:
        node = dq.popleft()
        for dst,dc in G[node].items():
            if done[dst] == 0:
                if done[node]!=dc:
                    done[dst] = dc
                else:
                    if dc == n:
                        done[dst] = 1
                    else:
                        done[dst] = dc+1
                dq.append(dst)
            

    for i in range(1,n+1):
        print(done[i])
main()
