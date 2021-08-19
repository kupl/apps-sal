def love_language(partner, weeks):
    return max(LOVE_LANGUAGES, key=lambda word: sum((partner.response(word) == 'positive' for _ in range(weeks))))
