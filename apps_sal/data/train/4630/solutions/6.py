def decrypt(s):
    (prev, c) = (int(s[-1]), 0)
    res = [prev]
    for d in s[::-1][1:]:
        x = int(d) - prev - c
        (prev, c) = ((x + 10) % 10, x < 0)
        res.append(prev)
    return 'impossible' if res[-1] == 0 else ''.join(map(str, res[::-1]))
