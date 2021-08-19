def center_of(chars):
    if not chars:
        return ''
    total = 0
    res = []
    for i in range(1, len(chars) * 2 + 1):
        if i % 2 == 1:
            res.append((i + 1) // 2 + total)
            res[-1] = chars[(res[-1] - 1) % len(chars)]
        total += i
    res = ''.join(res)
    for i in range(len(res) // 2 + 1):
        if len(res) % len(res[:i + 1]) != 0:
            continue
        if res[:i + 1] * (len(res) // len(res[:i + 1])) == res:
            return res[:i + 1]
    return res
