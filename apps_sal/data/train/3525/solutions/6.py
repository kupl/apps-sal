def flipping_game(num):
    all_pairs = ((i, j) for i in range(len(num)) for j in range(i + 1, len(num) + 1))
    ones = (sum(num[:i]) + j - i - sum(num[i:j]) + sum(num[j:]) for i, j in all_pairs)
    return max(ones)
