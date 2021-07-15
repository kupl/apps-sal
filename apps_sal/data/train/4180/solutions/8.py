def lottery(s):
    seen = set()
    return ''.join(seen.add(a) or a for a in s if a.isdigit() and a not in seen) or "One more run!"
