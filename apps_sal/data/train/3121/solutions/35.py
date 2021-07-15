def solve(numbers):
    for x in numbers:
        if not -x in numbers:
            return x
