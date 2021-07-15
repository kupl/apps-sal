from itertools import product


def adfgx_encrypt(plaintext, square):
    mapping = {s: c1 + c2 for s, (c1, c2) in zip(square, product("ADFGX", repeat=2))}
    mapping["i"] = mapping["j"] = mapping.get("i", mapping.get("j"))
    return "".join(mapping[c] for c in plaintext).upper()


def adfgx_decrypt(ciphertext, square):
    mapping = {c1 + c2: s for s, (c1, c2) in zip(square, product("ADFGX", repeat=2))}
    return "".join(
        mapping[c1 + c2] for (c1, c2) in zip(*[iter(ciphertext)] * 2)
    ).lower()
