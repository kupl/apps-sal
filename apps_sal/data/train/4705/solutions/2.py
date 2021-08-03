def find_a_b(numbers, c):
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] == c:
                return [numbers[i], numbers[j]]
