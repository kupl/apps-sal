alphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", "!", "?", " "]


def switcher(arr):
    return "".join([alphabet[int(i) - 1] for i in arr])
