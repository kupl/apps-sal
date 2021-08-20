def movie(card, ticket, perc):
    (A, B) = (ticket, card + ticket * perc)
    (prev, count) = (ticket * perc, 1)
    while A <= int(B) + 1:
        count += 1
        prev = prev * perc
        A += ticket
        B += prev
    return count
