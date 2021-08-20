from collections import defaultdict


def pair_of_shoes(shoes):
    shoe_counts = defaultdict(int)
    for (shoe_type, shoe_size) in shoes:
        shoe_counts[shoe_size] += 1 if shoe_type else -1
    return all((a == 0 for a in shoe_counts.values()))
