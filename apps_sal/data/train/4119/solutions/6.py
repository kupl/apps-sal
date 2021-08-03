emotions = {"T_T": 1, ":(": 2, ":|": 3, ":)": 4, ":D": 5}


def sort_emotions(lst, desc):
    return sorted(lst, key=emotions.get, reverse=desc)
