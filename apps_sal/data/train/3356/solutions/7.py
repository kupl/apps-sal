def three_amigos(numbers):
    return list(min((a for a in zip(numbers, numbers[1:], numbers[2:]) if sum(b % 2 for b in a) in [0, 3]), key=lambda x: max(x) - min(x), default=[]))
