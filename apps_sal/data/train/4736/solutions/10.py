def how_many_bees(hive):
    if hive == [] or hive == "" or hive == None:
        return 0
    result = 0
    for i in range(len(hive)):
        for k in range(len(hive[i])):
            if i > 1 and hive[i][k] == "b":
                if hive[i - 1][k] == "e" and hive[i - 2][k] == "e":
                    result += 1
            if i < len(hive) - 2 and hive[i][k] == "b":
                if hive[i + 1][k] == "e" and hive[i + 2][k] == "e":
                    result += 1
            if k < len(hive[i]) - 2 and hive[i][k] == "b":
                if hive[i][k + 1] == "e" and hive[i][k + 2] == "e":
                    result += 1
            if k > 1 and hive[i][k] == "b":
                if hive[i][k - 1] == "e" and hive[i][k - 2] == "e":
                    result += 1

    return result
