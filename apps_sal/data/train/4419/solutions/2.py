def reg_sum_hits(n, s):
    faces = list(range(1, s + 1))
    sums = []
    for r in range(n):
        if not sums:
            new_sums = [[f, 1] for f in faces]
        else:
            new_sums = []
            for (value, count) in sums:
                for f in faces:
                    new_sums.append([value + f, count])
            new_sums.sort()
            i = 0
            while i < len(new_sums) - 1:
                (a, b) = new_sums[i:i + 2]
                if a[0] == b[0]:
                    new_sums[i:i + 2] = [[a[0], a[1] + b[1]]]
                else:
                    i += 1
        sums = new_sums
    return sums
