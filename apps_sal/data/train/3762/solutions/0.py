def pattern(n):
    return '\n'.join(''.join(str((x + y) % n + 1) for y in range(n)) for x in range(n))
