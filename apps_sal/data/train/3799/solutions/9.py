def baubles_on_tree(baubles, branches):
    if not branches:
        return "Grandma, we will have to buy a Christmas tree first!"
    d, m = divmod(baubles, branches)
    return [d * (i <= branches) + (i <= m-1) for i in range(branches)]

