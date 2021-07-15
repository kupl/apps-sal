def solution(n):
    ROMAN_SYMBOLS = ["M", "D", "C", "L", "X", "V", "I"]
    ROMAN_VALUES = [1000, 500, 100, 50, 10, 5, 1]
    idx = 0
    roman = []
    while n > 0:
        if n < ROMAN_VALUES[idx]:
            idx += 1
            continue
        n -= ROMAN_VALUES[idx]
        roman.append(ROMAN_SYMBOLS[idx])
        if roman[-4:].count(roman[-1]) == 4:
            roman = roman[:-3] + [ROMAN_SYMBOLS[idx-1]]
            if roman[-3:-2] == roman[-1:]:
                roman = roman[:-3] + [ROMAN_SYMBOLS[idx]] + [ROMAN_SYMBOLS[idx-2]]
    return "".join(roman)
