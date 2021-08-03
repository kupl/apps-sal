def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total
