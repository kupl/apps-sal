def decrypt(text, n):
    if text:
        mid = len(text) // 2
        for _ in range(n):
            text = ''.join(sum(zip(text[mid:], list(text[:mid]) + ['']), ()))
    return text


def encrypt(text, n):
    if text:
        for _ in range(n):
            text = text[1::2] + text[::2]
    return text
