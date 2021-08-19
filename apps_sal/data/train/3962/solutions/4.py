def house_of_cards(floors):
    assert floors > 0
    return sum((2 + 3 * a for a in range(floors + 1)))
