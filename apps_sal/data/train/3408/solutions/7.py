def add_check_digit(n):
    rem = sum((i % 6 + 2) * int(d) for i, d in enumerate(n[::-1])) % 11
    return f"{n}{'0X987654321'[rem]}"
