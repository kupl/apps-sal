# chameleons is int[3], desiredColor is int from 0 to 2
def chameleon(chameleons, desiredColor):
    print(chameleons, desiredColor)
    other_coler = [j for i, j in enumerate(chameleons) if i != desiredColor]

    # 判断是否有解
    if sum([i == 0 for i in chameleons]) == 2 and chameleons[desiredColor] == 0:
        return -1
    elif not (other_coler[0] - other_coler[1]) % 3 == 0:
        return -1

    # 判断meet次数
    return max(other_coler)
