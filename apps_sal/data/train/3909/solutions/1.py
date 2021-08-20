def is_keith_number(n):
    (turn, seq) = (0, [int(d) for d in str(n)])
    while seq[-1] < n:
        seq = seq[1:] + [sum(seq)]
        turn += 1
    return n > 9 and seq[-1] == n and turn
