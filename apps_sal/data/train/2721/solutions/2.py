def pyramid(n):
    return "".join(
        f"{' ' * (n - i - 1)}/{(' ' if i < (n - 1) else '_') * i * 2}\\\n" for i in range(n)
    )

