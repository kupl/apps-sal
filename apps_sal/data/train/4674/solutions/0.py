def rank(st, we, n):
    if not st:
        return 'No participants'
    if n > len(we):
        return 'Not enough participants'

    def name_score(name, w):
        return w * (len(name) + sum([ord(c.lower()) - 96 for c in name]))
    scores = [name_score(s, we[i]) for (i, s) in enumerate(st.split(','))]
    scores = list(zip(st.split(','), scores))
    scores.sort(key=lambda x: (-x[1], x[0]))
    return scores[n - 1][0]
