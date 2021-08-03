def pattern(n):
    return '\n'.join(''.join(str(i + 1) for i in range(n)[j:]) for j in range(n))
