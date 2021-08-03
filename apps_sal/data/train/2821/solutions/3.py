def trim(beard):
    for row in range(0, len(beard)):
        for hair in range(0, len(beard[row])):
            if row != len(beard) - 1:
                beard[row][hair] = "|"
            else:
                beard[row][hair] = "..."

    return beard
