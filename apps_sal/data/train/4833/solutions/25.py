replace_exclamation = lambda s, r=__import__("re").sub: r(r'[aeiouAEIOU]', '!', s)
