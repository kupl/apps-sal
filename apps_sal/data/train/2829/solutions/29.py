def array_madness(a, b):
    SumA = 0
    for number in a:
        SumA += number ** 2
    SumB = 0
    for number in b:
        SumB += number ** 3
    return SumA > SumB
