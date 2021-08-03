def who_wins_beggar_thy_neighbour(hand_1, hand_2, MAX_PLAYED=10000):
    punishments = {"J": 1, "Q": 2, "K": 3, "A": 4}
    hands, common = [hand_1, hand_2], []
    cards_played, player_index = 0, 0

    def opponent_index(index):
        return (index + 1) % 2

    def play_card(index):
        nonlocal cards_played, common
        cards_played += 1
        card = hands[index][0]
        hands[index] = hands[index][1:]
        common.append(card)
        return card[0]

    def punish(index, v):
        nonlocal player_index, common
        # Play as many cards as mandated by punishments
        for i in range(punishments[v]):
            if player_won():
                return
            # If next card is special, stop and punish opponent
            val = play_card(index)
            if val in punishments:
                punish(opponent_index(index), val)
                return
        # Player completed their punishment so other player wins common
        player_index = opponent_index(index)
        hands[player_index].extend(common)
        common = []
        return

    def player_won():
        return not hands[0] or not hands[1]

    def get_winner():
        assert(player_won())
        if not hands[0]:
            return opponent_index(0)
        if not hands[1]:
            return opponent_index(1)

    # Driver code
    while(not player_won() and cards_played < MAX_PLAYED):
        # Play next card and set next player
        val = play_card(player_index)
        player_index = opponent_index(player_index)
        # If val is special, set next player with punish
        if val in punishments:
            punish(player_index, val)

    if player_won():
        return get_winner()
    return None
