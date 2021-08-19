def calc(cards):
    n = len(cards)

    table = [[-1 for i in range(n)] for j in range(n)]  # stores intermediate highest score
    high = n - 1

    def score(low, high, i):
        # base case
        if (i == n):
            return 2**i * cards[low]
        # looks up if we have already calculated highest score
        elif (table[low][high] != -1):
            return table[low][high]
        # recursive case
        else:
            max_score = max(score(low + 1, high, i + 1) + 2**i * cards[low],  # pick card on the left, LOW
                            score(low, high - 1, i + 1) + 2**i * cards[high])   # pick card on the right, HIGH
            table[low][high] = max_score

            return max_score

    return score(0, high, 1)
