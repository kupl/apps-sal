def cake(candles,debris):
    #your code here
    return 'Fire!' if candles*0.7 < sum([ord(c) if i%2 == 0 else ord(c)-96 for i, c in enumerate(debris)]) and candles != 0 else 'That was close!'
