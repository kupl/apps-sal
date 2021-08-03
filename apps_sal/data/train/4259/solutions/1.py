def pattern(n, x=1, *args):
    x = x if x > 1 else 1
    top = ["1" + "".join(" " * (2 * n - 3) + "1" for k in range(x))] if n > 1 else []
    wing = [" " + "".join(" " * (i - 2) + str(i % 10) + " " * (2 * (n - i) - 1) + str(i % 10) + " " * (i - 1) for k in range(x)) for i in range(2, n)]
    middle = [(str(n % 10) + "".join([" " * (2 * n - 3) + str(n % 10) for k in range(x - 1)])).center(2 * (n - 1) * x + 1)] if n > 1 else "1"
    return "\n".join(top + wing + middle + wing[::-1] + top) if n > 0 else ""
