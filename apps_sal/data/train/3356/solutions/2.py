from collections import defaultdict


def three_amigos(numbers):
    candidates = defaultdict(list)
    for i in range(len(numbers) - 2):
        triplet = numbers[i:i + 3]
        if len({n % 2 for n in triplet}) == 1:
            candidates[max(triplet) - min(triplet)].append(triplet)
    return candidates[min(candidates)][0] if candidates else []
