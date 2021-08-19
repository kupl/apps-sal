def pattern(n):
    lines = []
    for i in range(1, n + 1):
        line = ' ' * (n - i)
        line += ''.join((str(j % 10) for j in range(1, i + 1)))
        line += line[::-1][1:]
        lines.append(line)
    return '\n'.join(lines + lines[::-1][1:])
