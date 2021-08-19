def beasts(heads, tails):
    # your code here

    o = (5 * tails - heads) / 3
    h = (heads - 2 * tails) / 3

    if o == int(o) and h == int(h) and o >= 0 and h >= 0:
        return [int(o), int(h)]
    else:
        return "No solutions"
    # return [orthus, hydra]
