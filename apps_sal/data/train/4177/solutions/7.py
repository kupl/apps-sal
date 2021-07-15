def men_from_boys(arr):
    mens = [x for x in sorted(set(arr)) if x % 2 == 0]
    boys = [x for x in sorted(set(arr), key=lambda n: -n) if x % 2 == 1]
    return mens + boys
