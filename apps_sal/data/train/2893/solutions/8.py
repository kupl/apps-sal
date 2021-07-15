def plant_doubling(n):
    list = []
    for i in range(64):
        list.append(2**i)
    rounds = 0
    while n >= 1:
        relevant_list = []
        for item in list:
            if item <= n:
                relevant_list.append(item)
        n = n - relevant_list[-1]
        rounds = rounds + 1
    return rounds
