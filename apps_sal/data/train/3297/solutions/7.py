def will_it_balance(stick, terrain):
    c = 0
    T = []
    for i in range(len(stick)):
        c = c + i * stick[i]
    m = c / sum(stick)
    for i in range(len(terrain)):
        if terrain[i] == 1:
            T.append(i)

    return (len(T) >= 2 and T[0] <= m <= T[-1]) or (len(T) == 1 and T[0] == m)
