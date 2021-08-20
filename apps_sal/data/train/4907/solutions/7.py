def candles(candles1, leftovers):
    return candlesop(candles1, leftovers)


def candlesop(candles1, leftovers):
    candle1 = candles1
    answer = 0
    left = 0
    while candle1 != 0:
        answer += candle1
        left += candle1
        candle1 = left // leftovers
        left = left % leftovers
    return answer
