from collections import Counter
def first_non_repeating_letter(string):
    counts = Counter(string.lower())
    try:
        first_unique = next(item[0] for item in counts.items() if item[1]==1)
    except StopIteration:
        return ""
    if first_unique.upper() in string:
        return first_unique.upper()
    else:
        return first_unique
