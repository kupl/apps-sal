def array_madness(a,b):
    return sum(list(map(lambda elem : elem ** 2 , a))) > sum(list(map(lambda elem : elem ** 3 , b)))
