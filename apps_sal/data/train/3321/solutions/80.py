def evil(n):
    return 'It\'s Odious!' if n <= 2 or bin(n)[2:].count('1') % 2 else "It's Evil!"
