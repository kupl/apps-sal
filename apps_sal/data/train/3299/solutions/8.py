def calc(cards):
    n = len(cards)
    table = [[-1 for i in range(n)] for j in range(n)]
    high = n - 1

    def score(low, high, i):
        if i == n:
            return 2 ** i * cards[low]
        elif table[low][high] != -1:
            return table[low][high]
        else:
            max_score = max(score(low + 1, high, i + 1) + 2 ** i * cards[low], score(low, high - 1, i + 1) + 2 ** i * cards[high])
            table[low][high] = max_score
            return max_score
    return score(0, high, 1)
