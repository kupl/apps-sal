def update_inventory(cur_stock, new_stock):
    updated_stock = []
    stock = []
    brands = []
    tmpBrands = []

    for i in cur_stock:
        brands.append(i[1])

    for j in new_stock:
        if j[1] not in brands:
            brands.append(j[1])

    brands.sort()
    tmpBrands = brands.copy()
    print(tmpBrands)

    for i in cur_stock:
        for j in new_stock:
            if i[1] == j[1]:
                stock.append((i[0] + j[0], i[1]))
                tmpBrands.remove(i[1])

    for i in cur_stock:
        if i[1] in tmpBrands:
            stock.append(i)
            tmpBrands.remove(i[1])

    for j in new_stock:
        if j[1] in tmpBrands:
            stock.append(j)
            tmpBrands.remove(j[1])

    i = 0
    while len(stock):
        for j in brands:
            for k in stock:
                if j == k[1]:
                    updated_stock.append(k)
                    stock.remove(k)
                    break
        i += 1

    return updated_stock
