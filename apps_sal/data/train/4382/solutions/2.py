def uncollapse(s):
    return __import__('re').sub('(zero|one|two|three|four|five|six|seven|eight|nine)', ' \\1', s)[1:]
