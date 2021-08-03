def shift(string, step):
    i = (step % len(string)) if string else 0
    return f"{string[-i:]}{string[:-i]}"


def encode(n, string):
    for _ in range(n):
        shifted = shift(string.replace(" ", ""), n)
        l = [len(word) for word in string.split(" ")]
        string = " ".join(shift(shifted[sum(l[:i]):sum(l[:i + 1])], n) for i in range(len(l)))
    return f"{n} {string}"


def decode(string):
    n, string = int(string.partition(" ")[0]), string.partition(" ")[2]
    for _ in range(n):
        shifted = shift("".join(shift(word, -n) for word in string.split(" ")), -n)
        l = [len(word) for word in string.split(" ")]
        string = " ".join(shifted[sum(l[:i]):sum(l[:i + 1])] for i in range(len(l)))
    return string
