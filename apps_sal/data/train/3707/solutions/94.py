def sorter(textbooks):
    sortbooks = sorted([x.lower() for x in textbooks])
    out = []
    for sb in sortbooks:
        for tb in textbooks:
            if sb==tb.lower():
                out.append(tb)
    return out
