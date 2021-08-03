def comfortable_numbers(l, r):
    s = [sum(map(int, str(n))) for n in range(l, r + 1)]
    return sum(s[i] >= i - j <= s[j] for i in range(1, len(s)) for j in range(i))
