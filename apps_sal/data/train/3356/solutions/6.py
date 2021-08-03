def three_amigos(numbers):
    it = (xs for xs in zip(numbers, numbers[1:], numbers[2:]) if len({x % 2 for x in xs}) == 1)
    return list(min(it, key=lambda xs: max(xs) - min(xs), default=()))
