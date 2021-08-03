
TT = int(input())
alp = "abcdefghijklmnopqrstuvwxyz"

for loop in range(TT):

    n, m = list(map(int, input().split()))

    s = []

    for i in range(n):
        tmp = list(input())
        s.append(tmp)

    blf = False

    for i in range(m):

        now = []
        for x in range(m):
            now.append(s[0][x])

        for j in range(26):
            now[i] = alp[j]
            difnum = [0] * n

            for a in range(n):
                for b in range(m):
                    if s[a][b] != now[b]:
                        difnum[a] += 1

            if max(difnum) <= 1:
                print("".join(now))
                blf = True
                break
        if blf:
            break

    if not blf:
        print(-1)
