q = int(input())
for _ in range(q):
    n = int(input())
    up = input()
    down = input()
    pipe = []
    pipe.append(up)
    pipe.append(down)
    pos = 0
    can = True
    for i in range(n):
        if(pipe[pos][i] > "2"):
            pos ^= 1
            if(pipe[pos][i] <= "2"):
                can = False
                break
    if pos == 0:
        can = False
    if(can):
        print("YES")
    else:
        print("NO")
