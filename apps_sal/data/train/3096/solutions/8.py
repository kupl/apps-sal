def josephus(itemlist, interval):
    length = len(itemlist)

    if interval == 1:
        return itemlist

    count = 1
    disposal = []

    while len(disposal) != length:
        index = 0
        for item in itemlist:
            if count == interval:

                disposal.append(item)
                itemlist.pop(index)
                count = 1

                try:
                    print(itemlist[index])
                except:
                    break

            count += 1
            index += 1
    return disposal
