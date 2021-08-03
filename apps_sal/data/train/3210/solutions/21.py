def get_strings(city):
    counts = {}

    for c in city.lower():
        if c.isalpha():
            counts[c] = counts[c] + "*" if c in counts else "*"

    return ",".join([f"{c}:{a}" for (c, a) in counts.items()])
