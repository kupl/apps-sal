def hamming(n):
    bag = {1}
    for _ in range(n - 1):
        head = min(bag)
        bag.remove(head)
        bag |= {head * 2, head * 3, head * 5}
    return min(bag)
