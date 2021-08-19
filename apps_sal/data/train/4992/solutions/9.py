def bingo(card, numbers):
    card_copy = list(card)
    card_copy.remove(card_copy[0])
    card_copy[2][2] = 0
    numbers = [int(x[1:]) for x in numbers]
    marked_card = [[0 if card_copy[row][col] == 0 else 0 if card_copy[row][col] in numbers else 1 for col in range(5)] for row in range(5)]
    for row in range(5):
        if sum(marked_card[row]) == 0:
            return True
    for col in range(5):
        if sum([marked_card[row][col] for row in range(5)]) == 0:
            return True
    if sum([marked_card[position][position] for position in range(5)]) == 0:
        return True
    if sum([marked_card[row][col] for col in range(5) for row in range(5) if row + col == 4]) == 0:
        return True
    return False
