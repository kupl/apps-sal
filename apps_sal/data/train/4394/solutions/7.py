def men_still_standing(cards):
    sent_off_A = set()
    sent_off_B = set()
    for i, card in enumerate(cards):
        if card.endswith("R"):
            sent_off_B.add(card[1:-1]) if card[0] == "B" else sent_off_A.add(card[1:-1])
        elif card.endswith("Y") and cards[:i].count(card) > 0:
            sent_off_B.add(card[1:-1]) if card[0] == "B" else sent_off_A.add(card[1:-1])
        if len(sent_off_A) == 5 or len(sent_off_B) == 5:
            break
    return (11 - len(sent_off_A), 11 - len(sent_off_B))
