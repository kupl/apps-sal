from collections import Counter


def two_by_two(animals):
    if not animals:
        return False
    return {animal: 2 for animal, count in Counter(animals).items() if count > 1}
