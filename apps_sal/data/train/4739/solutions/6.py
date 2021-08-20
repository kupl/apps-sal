from bisect import bisect_right


def same_col_seq(val, k, col, seq=[], colors=[]):
    if not seq:

        def color(v):
            return {0: 'blue', 1: 'red', 2: 'yellow'}[v % 3]

        def next_val(n):
            return seq[-1] + n
        seq.append(1)
        colors.append('red')
        n = 2
        v = next_val(n)
        while True:
            seq.append(v)
            colors.append(color(v))
            if v > 40 * 10 ** 6:
                break
            n += 1
            v = next_val(n)
    res = []
    index = find_gt(seq, val)
    limit = val * 2 * k
    while True:
        if colors[index] == col:
            res.append(seq[index])
            if len(res) == k:
                break
        if seq[index] > limit and len(res) == 0:
            break
        index += 1
    return res


def find_gt(a, x):
    return bisect_right(a, x)
