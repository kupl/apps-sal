def baubles_on_tree(baubles, branches):
    if not branches:
        return 'Grandma, we will have to buy a Christmas tree first!'
    q, r = divmod(baubles, branches)
    return [q + 1] * r + [q] * (branches - r)
