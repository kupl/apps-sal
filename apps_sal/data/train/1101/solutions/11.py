
for _ in range(int(eval(input()))):
    N, C, K = list(map(int, input().split()))
    poss, lines, res = [0] * (K + 1), {}, 0
    for _ in range(N):
        a, b, c = list(map(int, input().split()))
        if c - 1 not in lines:
            lines[c - 1] = {a: 1}
        else:
            lines[c - 1][a] = lines[c - 1].get(a, 0) + 1
    era = list(map(int, input().split()))
    for c in range(C):
        if era[c] == 0:
            lines.pop(c, None)
    for c, mp in list(lines.items()):
        vals = list(mp.values())
        if len(vals) >= 3:
            vals.sort()
            s1, s2, s3 = sum(vals), sum(a**2 for a in vals), sum(a**3 for a in vals)
            full = (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
            res += full
            gain = {0: 0}
            idx = 0
            for j in range(era[c], K + 1, era[c]):
                vals[idx] -= 1
                old = vals[idx] + 1
                nw = vals[idx]
                if vals[idx] == 0:
                    idx += 1
                    if idx == len(vals):
                        break
                s1 -= 1
                s2 += nw**2 - old**2
                s3 += nw**3 - old**3
                gain[j] = full - (s1**3 - 3 * s1 * s2 + 2 * s3) // 6
            prev = poss
            poss = [max(prev[i - j] + gain[j] for j in list(gain.keys()) if j <= i) for i in range(K + 1)]
    print(res - max(poss))
