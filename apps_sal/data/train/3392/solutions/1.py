def sierpinski(n):
    lines = ["*"]
    for i in range(2, n+2):
        lines = [l.center(2**i - 1) for l in lines] + [f"{l} {l}" for l in lines]
    return "\n".join(lines)

