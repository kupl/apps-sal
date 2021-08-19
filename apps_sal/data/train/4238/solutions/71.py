def squares_needed(grains):
    if grains == 0:
        return 0
    else:
        high_square = 0
        tablet = []
        print(tablet)
        for i in range(0, 64):
            tablet.append(2 ** i)
        for i in range(0, 64):
            if sum(tablet[:i + 1]) >= grains:
                high_square = i + 1
                break
        return high_square
