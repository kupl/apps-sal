from collections import deque


def who_wins_beggar_thy_neighbour(hand_1, hand_2):
    hands = [deque(hand_1), deque(hand_2)]
    common = deque()
    penalty = 0
    player = 0
    special = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    for turn in range(100000):
        if len(common) == 0:
            if len(hands[0]) == 0:
                return 1
            if len(hands[1]) == 0:
                return 0
        if len(hands[player]) == 0:
            return 1 - player
        card = hands[player].popleft()
        common.append(card)
        if card[0] in special:
            player = 1 - player
            penalty = special[card[0]]
        elif penalty == 0:
            player = 1 - player
        else:
            penalty -= 1
            if penalty == 0:
                player = 1 - player
                while(len(common) > 0):
                    hands[player].append(common.popleft())
    return None
