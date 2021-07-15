def solve(s) -> str:
    naujas_listas = split(s)
    return max(naujas_listas)


def split(tekstas) -> list:
    groups = []
    newword = ""
    for x, i in enumerate(tekstas[0:]):
        if i.isnumeric():
            newword += i

        else:
            if newword != "":
                groups.append(int(newword))
                newword = ""

    if newword != "":
        groups.append(int(newword))

    return groups
