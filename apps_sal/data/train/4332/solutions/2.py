M, B, r, c, d, N = [0], set(), 0, 0, 0, 10000
for _ in range(N + 104):
    d, _ = ((d - 1) % 4, B.discard((r, c))) if (r, c) in B else ((d + 1) % 4, B.add((r, c)))
    r, c = r + [-1, 0, 1, 0][d], c + [0, 1, 0, -1][d]
    M.append(len(B))


def langtons_ant(n):
    return M[n] if n < N else 12 * ((n - N) // 104) + M[N + ((n - N) % 104)]
