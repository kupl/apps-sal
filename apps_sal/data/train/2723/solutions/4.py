numbers = 'zero one two three four five six seven eight nine'.split()


def average_string(s):
    try:
        ns = list(map(numbers.index, s.split()))
        return numbers[sum(ns) // len(ns)]
    except (ValueError, ZeroDivisionError):
        return 'n/a'
