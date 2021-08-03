sum_nested_numbers = r = lambda a, p=1: sum(n**p if n * 0 == 0else r(n, p + 1)for n in a)
