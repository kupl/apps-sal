def play_if_enough(hand, play):
    result = ""
    letter = set(play)
    if len(play) > len(play):
        return 0, hand
    for i in letter:
        if i not in hand or play.count(i) > hand.count(i):
            return 0, hand
        hand = hand.replace(i, "", play.count(i))
    return 1, hand
