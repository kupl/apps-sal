from collections import Counter

def play_if_enough(hand, play):
    hand, play = Counter(hand), Counter(play)
    played = not play - hand
    if played: hand -= play
    return played, ''.join(hand.elements())
