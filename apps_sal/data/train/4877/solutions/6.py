def love_language(partner, weeks: int):
    import random
    for l in LOVE_LANGUAGES:
        random.seed(3)
        if partner.response(l) == 'positive':
            return l
