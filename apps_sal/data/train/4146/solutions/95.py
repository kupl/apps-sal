def is_sorted_and_how(list):

    ascendList = list[:]
    ascendList.sort()

    descendList = list[:]
    descendList.sort(reverse=True)

    return "yes, ascending" if ascendList == list else \
        "yes, descending" if descendList == list else "no"
