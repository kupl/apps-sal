def distribution_of_candy(candies):
    if len(candies) == 1:
        return [0, candies[0]]
    (c, lst) = (0, candies)
    while True:
        lst = [i // 2 if i % 2 == 0 else (i + 1) // 2 for i in lst]
        lst2 = lst[-1:] + lst[:-1]
        lst = [i + j for (i, j) in zip(lst, lst2)]
        c += 1
        if len(set(lst)) == 1:
            return [c, lst[0]]
