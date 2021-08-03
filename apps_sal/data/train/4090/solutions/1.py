def get_animals_count(ln, hn, horn):
    c, ln, hn = horn // 2, ln - 2 * horn, hn - horn // 2
    return {"rabbits": (ln - 2 * hn) // 2, "chickens": 2 * hn - ln // 2, "cows": c}
