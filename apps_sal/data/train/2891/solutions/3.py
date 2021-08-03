def find_the_key(message, code):
    r = ''.join(str(a - b) for a, b in zip(code, [ord(c) - 96 for c in message]))

    for k in range(1, len(r) + 1):
        if all(c == r[:k][i % k] for i, c in enumerate(r)):
            return int(r[:k])
