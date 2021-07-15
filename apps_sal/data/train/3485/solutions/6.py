def separate_liquids(glass):
    liquids = [];
    comparing = { 'H' : 1.36, 'W' : 1.00, 'A' : 0.87, 'O' : 0.80 }
    for row in glass:
        liquids.extend(row)

    liquids.sort(key=lambda k: comparing[k], reverse=True)
    
    for i in range(len(glass)):
        for j in range(len(glass[0])):
            glass[i][j] = liquids.pop()

    return glass
