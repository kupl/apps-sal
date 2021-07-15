def solve(s):
    return max(find_numbers(s))


def find_numbers(chaos):
    numbers = []
    buffer = []
    for char in chaos:
        if char.isnumeric():
            buffer.append(char)
        elif char.isalpha() and buffer:
            numbers.append(int("".join(buffer)))
            buffer = []
    if buffer:
        numbers.append(int("".join(buffer)))
    return numbers
