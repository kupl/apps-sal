def movie(card, ticket, perc):
    import math
    i = 0
    sys_A = 0
    sys_B = card
    while True:
        i += 1
        sys_B += ticket*(perc**i)
        sys_A += ticket
        if math.ceil(sys_B) < sys_A:
            return i
