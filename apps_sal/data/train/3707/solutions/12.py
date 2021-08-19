def sorter(textbooks):
    textbooks.sort(key=lambda x: x.lower())
    # .sort() sorts the list while considering every element as if it is in lowercase
    return textbooks
