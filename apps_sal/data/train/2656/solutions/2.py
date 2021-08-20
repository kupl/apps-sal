def encode(bird):
    words = bird.replace('-', ' ').split()
    patterns = {1: (4,), 2: (2, 2), 3: (1, 1, 2), 4: (1, 1, 1, 1)}
    return ''.join(map(lambda w, l: w[:l], words, patterns[len(words)])).upper()


def bird_code(birds):
    return list(map(encode, birds))
