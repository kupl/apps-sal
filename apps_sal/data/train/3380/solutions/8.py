from itertools import groupby

def look_and_say_sequence(first_element, n):
    if first_element == "22": return "22"
    for _ in range(n-1):
        first_element = ''.join(f"{len(list(l))}{c}" for c,l in groupby(first_element))
    return first_element
