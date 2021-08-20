def find_polydivisible(digits_limit):
    numbers = []
    previous = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digits = 2
    poly_for_digits = []
    while previous and digits <= digits_limit:
        numbers += previous
        for p in previous:
            for i in range(10):
                number = p * 10 + i
                if number % digits == 0:
                    poly_for_digits.append(number)
        previous = poly_for_digits[:]
        poly_for_digits = []
        digits += 1
    return numbers


polydivisibles = find_polydivisible(26)


def next_num(n):
    return next((p for p in polydivisibles if p >= n + 1), None)
