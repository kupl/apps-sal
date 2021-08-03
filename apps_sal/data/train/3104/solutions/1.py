def reindeer(presents):
    assert presents <= 180
    return 2 + presents // 30 + (1 if presents % 30 else 0)
