def josephus(itemlist, interval):
    length = len(itemlist)

    if interval == 1:
        return itemlist

    count = 1
    disposal = []  # list which stores order in which items get deleted

    while len(disposal) != length:  # loop runs unti; every item has been deleted
        index = 0  # gives an index. Useful if there are duplicates of items in a list
        for item in itemlist:
            if count == interval:

                disposal.append(item)
                itemlist.pop(index)
                count = 1

                try:
                    print(itemlist[index])  # sees if there is another number after the deleted one. Catches numbers at the end of the list which get's deleted
                except:
                    break

            count += 1
            index += 1
    return disposal
