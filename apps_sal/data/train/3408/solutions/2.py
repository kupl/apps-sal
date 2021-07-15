def add_check_digit(n):
    rem = sum((i % 6 + 2) * int(d) for i, d in enumerate(n[::-1])) % 11
    return f"{n}{'X' if rem == 1 else 11 - rem if rem else 0}"
