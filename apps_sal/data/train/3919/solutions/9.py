def shuffled_array(lst):
    R = lst[:]
    R.remove(sum(R) // 2)
    return sorted(R)
