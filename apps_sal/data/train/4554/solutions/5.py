def play_if_enough(hand, play):
    p = [hand.count(i) - play.count(i) for i in sorted(set(list(play)))]
    d = all(x >= 0 for x in p)
    h = [i * hand.count(i) for i in sorted(set(list(hand))) if play.count(i) == 0]
    h_p = [i * (hand.count(i) - play.count(i)) for i in sorted(set(list(play)))]
    return (d, ''.join(h + h_p)) if d is True else (d, hand)
