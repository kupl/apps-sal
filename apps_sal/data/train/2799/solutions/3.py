def beasts(heads, tails):
    extraheads = heads - 2 * tails
    if extraheads % 3 != 0 or not (0 <= extraheads <= 3 * tails):
        return "No solutions"
    hydra = extraheads // 3
    orthus = tails - hydra
    return [orthus, hydra]
