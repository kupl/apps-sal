li, i, pos, d = ['red', 'yellow', 'blue'], 1, 1, {}
while i < 2000:
    d[pos] = li[(pos - 1) % 3]
    i += 1
    pos += i


def same_col_seq(after, k, need):
    req, status = [], 0
    for i, j in d.items():
        if i > after:
            status = 1
        if status:
            if j == need:
                req.append(i)
        if len(req) == k or i >= 2 * k * after:
            break
    return req
