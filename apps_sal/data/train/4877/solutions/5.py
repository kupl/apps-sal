def love_language(p, w):
    return max(LOVE_LANGUAGES, key=lambda x: sorted(map(p.response, w * [x])))
