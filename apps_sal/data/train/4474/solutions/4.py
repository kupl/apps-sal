def start_smoking(bars,boxes):
    n = (bars * 10 + boxes) * 18
    count = 0
    while n > 4:
        n,  rest = divmod(n, 5)
        count += n
        n += rest
    return (bars * 10 + boxes) * 18 + count

