def find_a_b(numbers,c):
    for i, a in enumerate(numbers, 1):
        for b in numbers[i:]:
            if a * b == c: return [a, b]
