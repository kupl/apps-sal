def men_still_standing(cards):
    red = []
    yellow = []
    still_playing = {"A": 11, "B": 11}

    for card in cards:
        if still_playing["A"] < 7 or still_playing["B"] < 7:
            break

        if card[-1::] == "Y" and card[:-1:] not in red:
            if card[:-1:] not in yellow:
                yellow.append(card[:-1:])
            elif card[:-1:] in yellow:
                red.append(card[:-1:])
                still_playing[card[:1:]] -= 1
        elif card[-1::] == "R" and card[:-1:] not in red:
            red.append(card[:-1:])
            still_playing[card[:1:]] -= 1

    return still_playing["A"], still_playing["B"]
