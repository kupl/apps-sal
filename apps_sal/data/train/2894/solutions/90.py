def triple_trouble(one, two, three):
    new = ""
    for j in range(0, len(one)):
        name = one[j] + two[j] + three[j]
        new += one[j] + two[j] + three[j]
    return new

ziel = triple_trouble("burn", "reds", "roll")
print(ziel)

