def adfgx_encrypt(plaintext, square):
    table = {c: "{}{}".format("ADFGX"[i // 5], "ADFGX"[i % 5]) for i, c in enumerate(square.replace("j", "i"))}
    return "".join(table[c] for c in plaintext.replace("j", "i"))


def adfgx_decrypt(ciphertext, square):
    table = {"{}{}".format("ADFGX"[i // 5], "ADFGX"[i % 5]): c for i, c in enumerate(square)}
    return "".join(table[c] for c in (ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)))
