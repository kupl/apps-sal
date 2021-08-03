def house_of_cards(floors):
    if floors < 1:
        raise Exception()
    return (floors + 1) * (3 * floors + 4) // 2
