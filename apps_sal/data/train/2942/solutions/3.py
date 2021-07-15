def fold_to(distance):
    if distance >= 0:
        return int(distance * 10000).bit_length()
