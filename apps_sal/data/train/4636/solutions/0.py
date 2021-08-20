(H, W) = (6, 8)
KEYBOARD = ['abcde123fghij456klmno789pqrst.@0uvwxyz_/\x0e ', 'ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/\x0e ', '^~?!\'"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡\x0e\x0e\x0e_/\x0e ']
MAP = [{c: (i // W, i % W) for (i, c) in enumerate(KEYBOARD[x])} for x in range(len(KEYBOARD))]


def manhattan(*pts):
    dxy = [abs(z2 - z1) for (z1, z2) in zip(*pts)]
    return 1 + sum((min(dz, Z - dz) for (dz, Z) in zip(dxy, (H, W))))


def tv_remote(words):
    (cnt, mod, was) = (0, 0, 'a')
    for c in words:
        while c not in KEYBOARD[mod]:
            cnt += manhattan(MAP[mod][was], MAP[mod]['\x0e'])
            was = '\x0e'
            mod = (mod + 1) % 3
        cnt += manhattan(MAP[mod][was], MAP[mod][c])
        was = c
    return cnt
