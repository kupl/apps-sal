def ulam_sequence(u0, u1, n):
    # set up variables
    seq = [u0, u1]
    candidates = (u0 + u1) * n * [0]
    candidates[u0 + u1] = 1
    num = u1 + 1

    for _ in range(n - 2):
        # find smallest candidate
        while candidates[num] != 1:
            num += 1
        # adjust list if needed
        if len(candidates) < num * 2:
            candidates.extend([0] * (num * 2 - len(candidates)))
        # calculate new candidates
        for x in seq:
            candidates[num + x] += 1
        # update sequence
        seq.append(num)
        num += 1

    return seq
