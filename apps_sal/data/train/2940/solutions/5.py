def repeats(s):
    numbers = set()

    for number in s:
        if number in numbers:
            numbers.remove(number)
        else:
            numbers.add(number)
    return sum(numbers)
