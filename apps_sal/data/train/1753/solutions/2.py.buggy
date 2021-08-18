history = {}


def least_bribes(bribes):
    nonlocal history

    history = {}

    return worst_case(0, len(bribes) - 1, bribes)


def worst_case(s, e, bribes):

    nonlocal history

    length = e - s + 1

    if length == 0:
        return 0

    elif length == 1:
        return bribes[s]

    elif length == 2:
        return bribes[s] + bribes[s + 1]

    elif length == 3:
        return max([bribes[s] + bribes[s + 1], bribes[s + 1] + bribes[s + 2]])

    else:
        key = str(s) + "_" + str(e)

        if not key in history:
            worst = []
            for i in range(length):
                worst.append(max([worst_case(s, s + i - 1, bribes) + bribes[s + i], worst_case(s + i + 1, e, bribes) + bribes[s + i]]))
            history[key] = min(worst)

        return history[key]
