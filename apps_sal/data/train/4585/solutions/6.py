repetitive = {"00": "0", "11": "2358134711", "14": "5914"}

def find(a, b, n):
    sequence = f"{a}{b}"
    while not sequence[-2:] in repetitive:
        sequence = f"{sequence}{sum(int(n) for n in sequence[-2:])}"
    length = len(sequence)
    if n >= length:
        sequence = repetitive[sequence[-2:]]
        n = (n - length) % len(sequence)
    return int(sequence[n])

