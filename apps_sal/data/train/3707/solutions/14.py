def sorter(textbooks):
    # use list.sort(), and instruct programme to ignore capitalisation
    textbooks.sort(key=str.lower)
    return(textbooks)
