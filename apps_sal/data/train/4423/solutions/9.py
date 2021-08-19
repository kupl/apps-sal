from collections import Counter


def ball_probability(balls):
    (bag, (call1, call2), replaced) = balls
    bag = Counter(bag)
    total = sum(bag.values())
    A = bag[call1] / total
    if not replaced:
        bag[call1] -= 1
        total -= 1
    B = bag[call2] / total
    return round(A * B, 3)
