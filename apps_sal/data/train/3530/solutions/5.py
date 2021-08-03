def asterisc_it(n):
    return "".join(["*" + str(char) if i > 0 and (int("".join(map(str, n))[i - 1] if isinstance(n, list) else str(n)[i - 1]) % 2 == 0) and (int("".join(map(str, n))[i] if isinstance(n, list) else str(n)[i]) % 2 == 0) else str(char) for i, char in enumerate("".join(map(str, n)) if isinstance(n, list) else str(n))])
