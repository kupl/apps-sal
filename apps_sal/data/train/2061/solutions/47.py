from collections import deque
inpl = lambda: list(map(int,input().split()))
def sign(x):
    return (x > 0) - (x < 0)
# s, x, y
trans = {(1,0,0),(1,1,0),(2,1,0),(2,0,1),(2,1,1),(3,0,0),(3,0,1)}
all_trans = [trans]
for i in range(3):
    w = set()
    for s, x, y in all_trans[-1]:
        ns = (s+1) % 4
        nx = -y
        ny = x
        w.add((ns,nx,ny))
    all_trans.append(w)

#print(all_trans)
V = {(1,1):0, (-1,1):1, (-1,-1):2, (1,-1):3}

que = deque([(0,0,0,0)])
bfs = dict()
bfs[(0,0,0)] = 0
while que:
    s, x, y, d = que.popleft()
    if d > 10:
        break
    for ns, dx, dy in all_trans[s]:
        nx = x + dx
        ny = y + dy
        if not (ns,nx,ny) in bfs:
            que.append((ns, nx, ny, d+1))
            bfs[(ns,nx,ny)] = d+1

T = int(input())
for _ in range(T):
    ax, ay, bx, by, cx, cy = inpl()
    if ax == bx:
        px, qx = ax, cx
    elif ax == cx:
        px, qx = ax, bx
    else:
        px, qx = bx, ax
    if ay == by:
        py, qy = ay, cy
    elif ay == cy:
        py, qy = ay, by
    else:
        py, qy = by, ay
    ps = V[(qx-px, qy-py)]

    ans = 0
    th1, th2 = 3, 3
    if abs(px) + abs(py) > th1:
        k = min(abs(px),abs(py))
        l = abs(abs(px)-abs(py))
        if l < th1:
            k -= (th1-l+1)//2
        px -= sign(px)*k
        py -= sign(py)*k
        ans += k*2
        if abs(px) > th2:
            m = abs(px) - th2
            px -= sign(px)*m
            ans += m*2
        elif abs(py) > th2:
            m = abs(py) - th2
            py -= sign(py)*m
            ans += m*2
    
    # print(px,px,py,bfs[(ps,px,py)])
    ans += bfs[(ps,px,py)]
    print(ans)

