def rot13(message):
    source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    target = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    code = {k: v for k, v in zip(source, target)}

    result = ""

    for c in message:
        if c not in code:
            result += c
            continue

        result += code[c]

    return result
