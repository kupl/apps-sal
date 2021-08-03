def to_bit(c):
    if c == "?":
        bit = 26
    else:
        bit = (ord(c) - ord('a'))
    return bit


T = int(input())
for _ in range(T):
    s = input()

    mask = 0
    for c in s:
        if c != "?":
            mask ^= 1 << to_bit(c)

    good_prefixes = []
    good_prefixes.append(mask & ((1 << to_bit("?")) - 1))
    for i in range(26):
        good_prefixes.append((mask ^ (1 << i)) | (1 << to_bit("?")))

    prefixes = {0: 1}

    res = 0
    current = 0
    for c in s:
        current ^= 1 << to_bit(c)
        for prefix in good_prefixes:
            res += prefixes.get(prefix ^ current, 0)
        prefixes[current] = prefixes.get(current, 0) + 1

    print(res)
