def tiy_fizz_buzz(s):
    return "".join(("Iron " * c.isupper() + "Yard" * (c.lower() in "aeiou")).strip() or c for c in s)
