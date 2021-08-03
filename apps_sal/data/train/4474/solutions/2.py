def start_smoking(bars, boxes):
    total = bars * 10 * 18 + boxes * 18
    n = total
    while total >= 1:
        total /= 5
        n += total
    return int(n)
