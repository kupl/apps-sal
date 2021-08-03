def sorter(textbooks):
    textbooks_low = [el.lower() for el in textbooks]

    textbooks_low_sorted = sorted(textbooks_low)

    testbooks_sorted_indexes = [textbooks_low.index(el) for el in textbooks_low_sorted]

    return [textbooks[ind] for ind in testbooks_sorted_indexes]
