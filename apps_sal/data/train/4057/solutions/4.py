def score_hand(cards):
    aces  = cards.count("A")
    score = sum( int(card) if card.isdigit() else 10 for card in cards ) + aces
    
    if score > 21:
        for _ in range(aces):
            score -= 10
            if score <= 21:
                break
    
    return score
