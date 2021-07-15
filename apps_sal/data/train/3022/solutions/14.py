def two_highest(mylist):
    if not isinstance(mylist, list):
        return False
    return sorted(list(set(mylist)), reverse=True)[:2]
