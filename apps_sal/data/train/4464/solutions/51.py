def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False


feast('brown bear', 'bear claw')
