def solve(arr):
    m = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in arr)
    difs = [m[i + 1] - m[i] - 1 for i in range(len(m) - 1)]
    difs.append(1440 - m[-1] + m[0] - 1)
    maxd = max(difs)
    return f"{str(maxd//60).zfill(2)}:{str(maxd%60).zfill(2)}"
