def word_search(query, seq):
    array = []
    for x in seq:
        if query.lower() in x.lower():
            array.append(x)
        else:
            pass
    if array != []:
        return array
    else:
        array = ['None']
        return array
