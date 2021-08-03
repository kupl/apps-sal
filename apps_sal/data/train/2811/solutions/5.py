def get_stream(s):
    return "".join(bin(ord(c))[2:].zfill(7) for c in s)


def parse_stream(s):
    return "".join(chr(int(c, 2)) for c in [s[i:i + 7] for i in range(0, len(s), 7)])


def get_next(s):
    return s[:max(s.find("0"), s.find("1"))] or s


def get_sequences(s):
    while s:
        n = get_next(s)
        s = s[len(n):]
        if n:
            yield n


def compose(n):
    return "0" * (2 - int(n[0])) + " " + "0" * len(n)


def decompose(s):
    s = s.split(" ")
    output = ""
    while s:
        output += ({"0": "1", "00": "0"})[s.pop(0)] * len(s.pop(0))
    return output


def send(s):
    return " ".join(compose(seq) for seq in get_sequences(get_stream(s)))


def receive(s):
    return parse_stream(decompose(s))
