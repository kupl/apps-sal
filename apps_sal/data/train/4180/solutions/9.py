def lottery(s):
    seen = set(); seen_add = seen.add; seq = [i for i in s if i in '0123456789']
    return ''.join(x for x in seq if not (x in seen or seen_add(x))) or "One more run!"
