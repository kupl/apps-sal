from math import ceil


def baubles_on_tree(baubles, branches):
    return [ceil((baubles - i) / branches) for i in range(0, branches)] if branches > 0 else 'Grandma, we will have to buy a Christmas tree first!'
