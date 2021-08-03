def f(x):
    return round(.02 * x ** 3 + 3.06 * x ** 2 + 105.6 * x - 895)


def souls(character, build):

    final_level = sum(build) - 83 + sum([1 if n in character else 0 for n in 'hissss'])
    start_level = 6 - sum([1 if n in character else 0 for n in "awful cccn"])
    souls_needed = sum([
        17 * l + 16 * 41 if l < 8 else 18 * l + 11 * 59 if l < 12 else f(l + 1) for l in range(start_level, final_level)
    ])

    return "Starting as a " + character + ", level " + str(final_level) + " will require " + str(souls_needed) + " souls."
