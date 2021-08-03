def triple_trouble(one, two, three):
    one = [item for item in one]
    two = [item for item in two]
    three = [item for item in three]
    new = []
    for i in range(0, len(one)):
        new.append(one[i] + two[i] + three[i])
    return "".join(new)
