def divide(weight):
    assert 1 <= weight <= 100
    if weight == 2:
        return False
    if weight % 2 == 0:
        return True
    else:
        return False
