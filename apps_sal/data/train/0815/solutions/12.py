# cook your dish here
p = [2,3,5,7,11,13,17]
ed = [(0,3), (0,1), (1,2), (1,4), (2,5), (3,4), (3,6), (4,5), (4,7), (5,8), (6,7), (7,8)]

x = (1, 2, 3, 4, 5, 6, 7, 8, 9)

av = {x: 0}
qu = [x]
while qu:
    cur= qu.pop(0)
    for e in ed:
        if cur[e[0]] + cur[e[1]] in p:
            nxt = list(cur)
            nxt[e[0]], nxt[e[1]] = nxt[e[1]], nxt[e[0]]
            nxt = tuple(nxt)
            if nxt not in av:
                av[nxt] = av[cur] + 1 
                qu.append(nxt)

for _ in range(int(input())):
    input()
    grid = ()
    for i in range(3):
        grid += tuple(map(int, input().split()))
    print(av[grid] if grid in av else -1)
