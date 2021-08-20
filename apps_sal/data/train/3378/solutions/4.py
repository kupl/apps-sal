def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    half_len = len(encrypted_text) // 2
    (left, right) = (encrypted_text[:half_len], encrypted_text[half_len:])
    encrypted_text = [''.join(i) for i in zip(right, left)]
    if len(right) > half_len:
        encrypted_text += right[-1]
    return decrypt(''.join(encrypted_text), n - 1)


def encrypt(text, n):
    if n < 1:
        return text
    for _ in range(n):
        text = text[1::2] + text[0::2]
    return text
