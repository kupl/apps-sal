T = int(input())
for i in range(0, T):
    N, Q = map(int, input().split())
    s = [int(x) for x in input().split()]
    L = sorted(s)
    G = L[::-1]
    for j in range(0, Q):
        x, y = map(int, input().split())
        ans1 = abs(s[y - 1] - s[x - 1]) + y - x
        print(ans1, end=" ")

        pos1 = 0
        pos2 = N

        for k in range(0, len(L)):
            if(L[k] < min(s[x - 1], s[y - 1])):
                pos1 = k
            elif(L[k] == min(s[x - 1], s[y - 1])):
                pos1 = k
                break
            else:
                break

        for k in range(0, len(L)):
            if(G[k] > max(s[x - 1], s[y - 1])):
                pos2 = N - k - 1
            elif(G[k] == max(s[x - 1], s[y - 1])):
                pos2 = N - k - 1
                break
            else:
                break

        print(pos2 - pos1 + 1)
