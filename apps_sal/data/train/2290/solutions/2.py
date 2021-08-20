mod = 1000000007
eps = 10 ** (-9)


def main():
    import sys
    input = sys.stdin.readline

    def largest_rectangle_histogram(A):
        A.append(0)
        N = len(A)
        ret = 0
        st = [-1]
        left = [0] * N
        for i in range(N):
            while A[st[-1]] >= A[i]:
                ret = max(ret, (A[st[-1]] + 1) * (i - left[st[-1]]))
                st.pop()
                if not st:
                    break
            if st:
                left[i] = st[-1]
            else:
                left[i] = -1
            st.append(i)
        return ret

    def largest_rectangle_grid(grid, ok=1, ng=0):
        H = len(grid)
        W = len(grid[0])
        hist = [[0] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w] == ok:
                    hist[h][w] = hist[h - 1][w] + 1
        ret = 0
        for h in range(H):
            ret = max(ret, largest_rectangle_histogram(hist[h]))
        return ret
    (H, W) = list(map(int, input().split()))
    grid = []
    for _ in range(H):
        grid.append(input().rstrip('\n'))
    corner = [[0] * (W - 1) for _ in range(H - 1)]
    for h in range(H - 1):
        for w in range(W - 1):
            cnt = 0
            if grid[h][w] == '#':
                cnt += 1
            if grid[h + 1][w] == '#':
                cnt += 1
            if grid[h][w + 1] == '#':
                cnt += 1
            if grid[h + 1][w + 1] == '#':
                cnt += 1
            if cnt % 2 == 0:
                corner[h][w] = 1
    print(max(largest_rectangle_grid(corner), H, W))


def __starting_point():
    main()


__starting_point()
