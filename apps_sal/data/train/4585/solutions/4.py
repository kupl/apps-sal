def find(a, b, n):
    bag, seq = {}, [a, b]
    while True:
        if (a, b) in bag: break
        bag[a, b] = len(seq)
        a, b = b, a+b
        if b > 9:
            a, b = divmod(b, 10)
            seq.append(a)
        seq.append(b)
    return seq[n] if n < len(seq) else \
        seq[bag[a, b] + (n - bag[a, b]) % (len(seq) - bag[a, b])]

