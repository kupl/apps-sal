def decrypt(text, n):
    if not text:
        return text
    half = len(text) // 2
    arr = list(text)
    for _ in range(n):
        (arr[1::2], arr[::2]) = (arr[:half], arr[half:])
    return ''.join(arr)


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
