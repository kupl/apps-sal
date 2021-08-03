def reverse_number(n):
    return int(str(n)[::-1] if "-" not in str(n) else "-" + (str(n).replace("-", ""))[::-1])
