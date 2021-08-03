def sorter(textbooks):
    index = {word.lower(): word for word in textbooks}
    keys = sorted(index.keys())
    return [index[key] for key in keys]
