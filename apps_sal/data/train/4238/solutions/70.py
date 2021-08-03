def squares_needed(grains):
    # your code here
    if grains == 0:
        return 0
    else:
        return len(str(bin(grains))) - 2
