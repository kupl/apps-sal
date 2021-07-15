def odd_ones_out(numbers):
    dup = 0
    sec = list(set(numbers))
    for i in range(0, len(sec)):
        dup = 0
        for j in range(0, len(numbers)):
            if sec[i] == numbers[j]:
                dup = dup + 1
        if dup % 2 == 1:
            numbers = [value for value in numbers if value != sec[i]]
    return numbers
