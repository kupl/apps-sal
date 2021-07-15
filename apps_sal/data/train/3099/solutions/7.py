from string import ascii_uppercase, ascii_lowercase
from collections import Counter
import re

A = {x: i for i, x in enumerate(ascii_uppercase + ascii_lowercase)}

def f(P, W):
    row, col = divmod(P, W)
    r = [
        [row * W + i for i in range(W)],
        [W * i + col for i in range(W)]
    ]
    if P >= (W + 1) * row:
        s = P - row * (W + 1)
        r.append([s + (W + 1) * i for i in range(W - s)])
    else:
        s = W * (row - col)
        r.append([s + (W + 1) * i for i in range(W - row + col)])
    ###
    if P >= (W - 1) * (row + 1):
        s = W * (W - 2) + col + row + 1
        r.append([s - (W - 1) * i for i in range(W - s % W)])
    else:
        s = W * row + W * col
        r.append([s - (W - 1) * i for i in range(s // W + 1)])
    return r

def whoIsWinner(G, n, w, d="Draw"):
    if n > w: return d
    D, P, C = dict(), Counter(), Counter()
    for x in G:
        p, t = x.split("_")
        col = A[p]
        rp = col + P[col] * w
        P[col] += 1
        D[rp] = t
        C[t] += 1
        if C[t] < n:
            continue
        if next((1 for x in f(rp, w) if re.search(fr"({t})\1{{{n-1}}}", "".join(D.get(y, ".") for y in x))), None):
            return t
    return d
