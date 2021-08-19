def how_many_bees(hive):
    if hive == None or len(hive) == 0:
        return 0
    result = 0
    for i in range(len(hive[0])):
        test = ''
        for item in hive:
            test += item[i]
        result += test.count('bee')
        result += test.count('eeb')
    for i in range(len(hive)):
        test = ''
        for item in hive[i]:
            test += item
        result += test.count('bee')
        result += test.count('eeb')
    return result
