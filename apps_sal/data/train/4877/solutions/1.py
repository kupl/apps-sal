def love_language(partner, weeks):
    n = len(LOVE_LANGUAGES)
    count = [0] * n
    for i in range (0, weeks * 7):
        response = partner.response(LOVE_LANGUAGES[i % n])
        count[i % n] += 1 if response == 'positive' else 0
    return LOVE_LANGUAGES[count.index(max(count))]
