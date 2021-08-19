def disarium_number(number: int) -> str:
    powers = sum((pow(int(n), i) for (i, n) in enumerate(str(number), 1)))
    return 'Disarium !!' if powers == number else 'Not !!'
