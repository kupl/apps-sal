def triple_trouble(one, two, three):
    collector = ""
    size = 0

    while size < len(one):
        collector += one[size] + two[size] + three[size]
        size += 1

    return collector
