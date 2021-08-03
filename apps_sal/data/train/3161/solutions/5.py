def select(memory):
    names = memory.split(", ")
    hated = set()

    for idx, name in enumerate(names):
        if name[0] == "!":
            hated |= set(n.strip("!") for n in names[idx: idx + 2])

    return ", ".join(name for name in names if name.strip("!") not in hated)
