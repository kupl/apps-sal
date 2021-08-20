import collections


def play_if_enough(hand, play):
    (hand_counter, play_counter) = (collections.Counter(hand), collections.Counter(play))
    return (False, hand) if play_counter - hand_counter else (True, ''.join((hand_counter - play_counter).elements()))
