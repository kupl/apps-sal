def reindeer(presents):
    if presents > 180:
        raise Exception('Error')
    return 2 + int((presents + 29) / 30)
