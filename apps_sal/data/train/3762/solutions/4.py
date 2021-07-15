def pattern(s):
    return "\n".join(["".join((str(x + y) if x + y <= s else str(x + y - s * ((x + y) // s)) for y in range(s))) for x in range(1, s + 1)])
