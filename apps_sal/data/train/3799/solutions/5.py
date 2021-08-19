def baubles_on_tree(b, c):
    return [(b + c - i - 1) // c for i in range(c)] if c else 'Grandma, we will have to buy a Christmas tree first!'
