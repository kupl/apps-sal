SYMBOLS = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))


def solution(input):
    if not input:
        return 0
    for (char, value) in SYMBOLS:
        if input.startswith(char):
            return value + solution(input[len(char):])
