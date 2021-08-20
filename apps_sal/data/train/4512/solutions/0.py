masks = [0] * 10
for i in range(10 ** 4):
    for c in str(i):
        masks[int(c)] |= 1 << i


def find_num(n):
    (seq, x) = (1, 0)
    for j in range(n):
        M = seq
        for m in masks:
            if x & m:
                M |= m
        x = ~M & M + 1
        seq |= x
    return x.bit_length() - 1
