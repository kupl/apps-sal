def to_leet_speak(str):

    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "@8(D3F6

    transform=dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in str)
