def dont_give_me_five(start, end):
    arr = list(range(start, end + 1))
    filter = []
    for el in arr:
        if str(el).find('5') == -1:
            filter.append(el)
    print(filter)
    return len(filter)
