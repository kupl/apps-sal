def stairs(n):
    return "\n".join(step(i).rjust(4 * n - 1) for i in range(1, n+1))


def step(n):
    h = " ".join(str(i % 10) for i in range(1, n+1))
    return f"{h} {h[::-1]}"
