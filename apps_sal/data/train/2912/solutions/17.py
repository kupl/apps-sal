def find_multiples(integer, limit):
    return list(range(integer, limit + integer, integer)) if limit % integer == 0 else list(range(integer, limit, integer))
