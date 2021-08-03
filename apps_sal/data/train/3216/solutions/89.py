def movie(card, ticket, perc):
    import math
    SystemB = card
    for num in range(1, 500_000):
        SystemB += ticket * perc ** num
        if num * ticket > math.ceil(SystemB):
            break
    return num
