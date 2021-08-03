def ulam_sequence(u0, u1, n):
    seq = [u0, u1]
    sums = {u0 + u1}
    unique_sums = {u0 + u1}
    for i in range(n - 3):
        next_num = min(unique_sums)
        for num in seq:
            n = num + next_num
            if n not in sums:
                sums.add(n)
                unique_sums.add(n)
            else:
                if n in unique_sums:
                    unique_sums.remove(n)
        unique_sums.remove(next_num)
        seq.append(next_num)
    seq.append(min(unique_sums))
    return seq
