def word_to_bin(w):
    return [f"{bin(ord(c))[2:]:0>8}" for c in w]
