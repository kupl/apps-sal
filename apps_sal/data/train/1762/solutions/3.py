import re
def O(Q, W, E): return W <= Q <= E if W < E else E <= Q <= W


def mouse_path(Q):
    M, U, D, R, C = [], 0, 0, 0, 0
    for Q in re.findall('.\d+', 'R' + Q):
        D, Q = D + ('O' < Q or 3), int(Q[1:])
        r, c = [-Q, 0, Q, 0][D % 4] + R, [0, Q, 0, -Q][D % 4] + C
        U += R * c - r * C
        for H, W, h, w in M[:-1]:
            if (R == r) ^ (H == h):
                if O(R, H, h) and O(W, C, c) if H - h else O(H, R, r) and O(C, W, w) and not 0 == r == c == H == W:
                    return
            elif R == r == H and (O(C, W, w) or O(c, W, w) or O(W, C, c)) or C == c == W and (O(R, H, h) or O(r, H, h) or O(H, R, r)):
                return
        M.append((R, C, r, c))
        R, C = r, c
    if 0 == R == C:
        return abs(U + R - C) / 2
