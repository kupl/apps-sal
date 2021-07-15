def house_of_cards(floors):
    assert isinstance(floors, int) and floors > 0
    return (floors + 1) * (3 * floors + 4) // 2
