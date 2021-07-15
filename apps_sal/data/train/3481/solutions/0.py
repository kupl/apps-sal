def get_char_count(s):
    counts = {}
    for c in (c.lower() for c in s if c.isalnum()):
        counts[c] = counts[c] + 1 if c in counts else 1
    m = {}
    for k, v in counts.items():
        m[v] = sorted(m[v] + [k]) if v in m else [k]
    return m
