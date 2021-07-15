def define_suit(card: str) -> str:
    return (
        "clubs"
        if "C" in card
        else "diamonds"
        if "D" in card
        else "hearts"
        if "H" in card
        else "spades"
    )
