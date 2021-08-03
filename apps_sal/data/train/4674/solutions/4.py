from string import ascii_lowercase


def rank(st, we, n):
    names = st.split(",")
    ranks = {}

    if st == "":
        return "No participants"

    if n > len(names):
        return "Not enough participants"

    for index, name in enumerate(names):
        som = len(name) + sum([ascii_lowercase.index(letter) + 1 for letter in name.lower()])
        ranks[name] = we[index] * som

    sort = sorted(list(ranks.items()), key=lambda x: (-x[1], x[0]))
    return [name for name, som in sort][n - 1]
