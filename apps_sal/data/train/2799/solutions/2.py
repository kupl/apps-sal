def beasts(heads, tails):
    if heads not in range(tails * 2, tails * 5 + 1, 3):
        return 'No solutions'
    return [(tails * 5 - heads) / 3, (heads - tails * 2) / 3]
