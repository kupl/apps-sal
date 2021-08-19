def f(s):
    if ''.join(sorted(s)) == s:
        return ''
    ss = s[1:]
    if ''.join(sorted(ss)) == ss:
        xs = sorted(s, reverse=True)
        next_1st_digit = max((x for x in set(xs) if x < s[0]))
        xs.remove(next_1st_digit)
        return next_1st_digit + ''.join(sorted(xs, reverse=True))
    return s[0] + str(f(ss))


def next_smaller(n):
    s = f(str(n))
    return int(s) if s and (not s.startswith('0')) else -1
