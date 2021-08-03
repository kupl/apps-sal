def how_many_bees(hive):
    if not hive:
        return 0
    new_hive = [[i for i in line] for line in hive]
    result = 0
    for line in range(len(hive)):
        for i in range(len(hive[0])):
            if hive[line][i] == "b":
                if len(hive[0]) - i > 2 and hive[line][i + 1] == "e" and hive[line][i + 2] == "e":
                    result += 1
                if i > 1 and hive[line][i - 1] == "e" and hive[line][i - 2] == "e":
                    result += 1
                if len(hive) - line > 2 and hive[line + 1][i] == "e" and hive[line + 2][i] == "e":
                    result += 1
                if line > 1 and hive[line - 1][i] == "e" and hive[line - 2][i] == "e":
                    result += 1
                if len(hive[0]) - i > 2 and len(hive) - line > 2 and hive[line + 1][i + 1] == "e" and hive[line + 2][i + 2] == "e":
                    result += 1
                if i > 1 and line > 1 and hive[line - 1][i - 1] == "e" and hive[line - 2][i - 2] == "e":
                    result += 1
                if len(hive[0]) - i > 2 and line > 1 and hive[line - 1][i + 1] == "e" and hive[line - 2][i + 2] == "e":
                    result += 1
                if i > 1 and len(hive) - line > 2 and hive[line + 1][i - 1] == "e" and hive[line + 2][i - 2] == "e":
                    result += 1

    return result
