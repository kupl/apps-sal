def candles(m, n):
    answer = 0
    candles, leftovers = m, 0
    while candles >= 1 or leftovers >= n:
        answer += candles
        leftovers += candles
        candles = leftovers // n
        leftovers -= leftovers // n * n
    return answer
