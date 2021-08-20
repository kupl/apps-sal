def ulam_sequence(u0, u1, n):
    seq = [u0, u1]
    candidates = (u0 + u1) * n * [0]
    candidates[u0 + u1] = 1
    num = u1 + 1
    for _ in range(n - 2):
        while candidates[num] != 1:
            num += 1
        if len(candidates) < num * 2:
            candidates.extend([0] * (num * 2 - len(candidates)))
        for x in seq:
            candidates[num + x] += 1
        seq.append(num)
        num += 1
    return seq
