def get_issuer(number):
  # code your solution here
    card = list(int(x) for x in str(number))
    if len(card) == 15:
        if card[0] == 3:
            if card[1] == 4 or card[1] == 7:
                return "AMEX"
        else:
            return "Unknown"
    elif len(card) == 13:
        if card[0] == 4:
            return "VISA"
        else:
            return "Unknown"
    elif len(card) == 16:
        if card[0:4] == [6, 0, 1, 1]:
            return "Discover"
        elif card[0] == 4:
            return "VISA"
        elif card[0] == 5:
            if card[1] in range(1, 6):
                return "Mastercard"
            else:
                return "Unknown"
        else:
            return "Unknown"
    else:
        return "Unknown"
