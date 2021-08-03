def find_a_b(numbers, c):
    for i in numbers:
        if i != 0 and c / i in numbers[numbers.index(i) + 1:]:
            return [i, c / i]
