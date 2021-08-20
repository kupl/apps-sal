def sorter(textbooks):
    """Function that sort a list full of textbooks by subject"""
    return sorted(textbooks, key=str.lower)
