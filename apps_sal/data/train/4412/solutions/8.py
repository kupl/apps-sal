def get_partitionr(ss):
    out = []
    if len(ss) <= 1:
        return [ss]
    for i in range(2 ** len(ss) // 2):
        parts = [[], []]
        for item in ss:
            parts[i & 1].append(item)
            i >>= 1
        bb = get_partitionr(parts[1])
        for b in bb:
            out.append([parts[0]] + b)
    return out


def add(parts):
    total = 0
    for part in parts:
        total += sum((int(''.join(p)) if isinstance(p, list) else int(p) for p in part))
    return total


def find(n, z):
    parts = get_partitionr(list(str(n)))[1:]
    add_parts = add(parts)
    target = add_parts + z
    while add_parts <= target:
        n += 1
        parts = get_partitionr(list(str(n)))[1:]
        add_parts = add(parts)
    return n
