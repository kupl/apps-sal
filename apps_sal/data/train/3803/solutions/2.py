def update_inventory(cur_stock, new_stock):
    updated_stock = []
    stock = []
    brands = []
    tmpBrands = []

    # determine original brands available
    for i in cur_stock:
        brands.append(i[1])

    # determine all brands now available
    for j in new_stock:
        if j[1] not in brands:
            brands.append(j[1])

    # sort the brand list into alphabetical order
    brands.sort()
    tmpBrands = brands.copy()
    print(tmpBrands)

    # create list of summed intersecting stock
    for i in cur_stock:
        for j in new_stock:
            if i[1] == j[1]:
                stock.append((i[0] + j[0], i[1]))
                # remove brand from list
                tmpBrands.remove(i[1])

    # add mutually exclusive brand stock from original stock
    for i in cur_stock:
        if i[1] in tmpBrands:
            stock.append(i)
            tmpBrands.remove(i[1])

    # add mutually exclusive brand stock from new stock
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
