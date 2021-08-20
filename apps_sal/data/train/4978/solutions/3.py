def encode(n, cleartext):

    def rotate_right(sequence, n):
        n %= len(sequence) or 1
        return sequence[-n:] + sequence[:-n]
    for _ in range(n):
        letters = iter(rotate_right([c for c in cleartext if c != ' '], n))
        cleartext = ''.join((c if c == ' ' else next(letters) for c in cleartext))
        cleartext = ' '.join((rotate_right(word, n) for word in cleartext.split(' ')))
    return f'{n} {cleartext}'


def decode(ciphertext):

    def rotate_left(sequence, n):
        n %= len(sequence) or 1
        return sequence[n:] + sequence[:n]
    (n, ciphertext) = ciphertext.split(' ', 1)
    n = int(n)
    for _ in range(n):
        ciphertext = ' '.join((rotate_left(word, n) for word in ciphertext.split(' ')))
        letters = iter(rotate_left([c for c in ciphertext if c != ' '], n))
        ciphertext = ''.join((c if c == ' ' else next(letters) for c in ciphertext))
    return ciphertext
