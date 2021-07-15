def hot_singles(lst1, lst2):
    return sorted(set(lst1) ^ set(lst2), key=(lst1 + lst2).index)
