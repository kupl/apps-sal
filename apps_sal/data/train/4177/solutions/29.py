def men_from_boys(arr):
    men = [x for x in set(arr) if x % 2 == 0]
    boizz = [x for x in set(arr) if x % 2 != 0]

    return sorted(men) + sorted(boizz, reverse=True)
