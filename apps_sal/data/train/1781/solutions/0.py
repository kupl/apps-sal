def who_wins_beggar_thy_neighbour(*hands, special_cards='JQKA'):
    hands = [list(reversed(hand)) for hand in hands]
    (player, deck_length) = (0, sum(map(len, hands)))
    (deal_start, deal_value, common) = (None, 0, [])
    while len(hands[player]) < deck_length:
        if deal_start == player:
            hands[player] = common[::-1] + hands[player]
            (deal_start, deal_value, common) = (None, 0, [])
            continue
        for _ in range(min(deal_value or 1, len(hands[player]))):
            card = hands[player].pop()
            common.append(card)
            if card[0] in special_cards:
                (deal_start, deal_value) = (player, special_cards.index(card[0]) + 1)
                break
        player = (player + 1) % len(hands)
    return player
