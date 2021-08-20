from collections import Counter


def count_feelings(stg, lst):
    letters = Counter(stg)
    count = sum((1 for feeling in lst if not Counter(feeling) - letters))
    return f"{count} feeling{('s' if count != 1 else '')}."
