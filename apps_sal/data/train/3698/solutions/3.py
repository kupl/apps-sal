def tiy_fizz_buzz(stg):
    return "".join("Iron Yard" if c in "AEIOU" else "Yard" if c in "aeiou" else "Iron" if c.isupper() else c for c in stg)
