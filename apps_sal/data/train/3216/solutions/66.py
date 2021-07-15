def movie(card, ticket, perc):
    result = 1
    B = card+ticket*perc
    while ticket*result < B+1:
        result += 1
        B += ticket*perc**result
    return result
