def jumbled_string(s, n):
    seen = []
    while s not in seen:
        seen.append(s)
        s = f'{s[::2]}{s[1::2]}'
    return seen[n % len(seen)]
