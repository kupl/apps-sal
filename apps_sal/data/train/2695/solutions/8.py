from collections import Counter

def pair_of_shoes(shoes):
    def count_of_type(type_):
        return Counter(n for t, n in shoes if t == type_)
    return count_of_type(0) == count_of_type(1)
