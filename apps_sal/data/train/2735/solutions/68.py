def jumping_number(number: int) -> str:
    digits = list(map(int, str(number)))
    return "Jumping!!" if all(abs(j - i) == 1 for i, j in zip(digits, digits[1:])) else "Not!!"
