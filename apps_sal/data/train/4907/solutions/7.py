def candles(candles1, leftovers):
    return candlesop(candles1, leftovers)


# Candle operations.
def candlesop(candles1, leftovers):
    candle1 = candles1
    answer = 0
    left = 0
    # while loop; as long as some candles remain, the loop keeps running.
    while candle1 != 0:
        answer += candle1
        left += candle1
        candle1 = left // leftovers
        left = left % leftovers
    return answer
