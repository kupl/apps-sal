def get_score(dice):
    freq = {e: dice.count(e) for e in set(dice)}
    score = 0

    if all(e in freq for e in range(1, 7)):
        return 1000

    if len(freq) is 3 and all(e is 2 for e in freq.values()):
        return 750

    for d in range(1, 7):
        if d in freq and freq[d] is 6:
            return d * 4000 if d is 1 else d * 400
        elif d in freq and freq[d] is 5:
            score += d * 3000 if d is 1 else d * 300
            del freq[d]
        elif d in freq and freq[d] is 4:
            score += d * 2000 if d is 1 else d * 200
            del freq[d]
        elif d in freq and freq[d] is 3:
            score += d * 1000 if d is 1 else d * 100
            del freq[d]

    score += freq[1] * 100 if 1 in freq else 0
    score += freq[5] * 50 if 5 in freq else 0

    return "Zonk" if score is 0 else score
