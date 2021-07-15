def squares_needed(grains):
    if not grains:
        return 0
    else:
        return len(str(bin(grains)))-2
