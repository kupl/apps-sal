def men_still_standing(cards):
    A_sentoff = set()
    B_sentoff = set()

    for index, card in enumerate(cards):
        if card[-1] == "R":
            A_sentoff.add(card[1:-1]) if card[0] == "A" else B_sentoff.add(card[1:-1])
        elif card[-1] == "Y" and cards[:index].count(card) > 0:
            A_sentoff.add(card[1:-1]) if card[0] == "A" else B_sentoff.add(card[1:-1])

        if len(A_sentoff) == 5 or len(B_sentoff) == 5:
            break

    a_remaining = 11 - len(A_sentoff)
    b_remaining = 11 - len(B_sentoff)

    return (a_remaining, b_remaining)
