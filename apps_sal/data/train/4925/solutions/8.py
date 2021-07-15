def collatz(n):
    collatz = str(n) + '->'
    while n != 1:
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        collatz += str(n) + '->'
    return collatz.rstrip('->')
