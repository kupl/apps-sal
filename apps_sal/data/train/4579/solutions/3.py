def pattern(n):
    return "\n".join("".join(str(max(r, c) % 10) for c in range(n, 0, -1)) for r in range(n, 0, -1))
