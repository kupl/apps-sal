def triple_trouble(one, two, three):
    new_line = ""
    for i in range(0, len(one)):
        new_line += one[i] + two[i] + three[i]
    return new_line
