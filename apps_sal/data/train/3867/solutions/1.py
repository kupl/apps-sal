def remove_rotten(fruit_bag):
    # Checking
    if not fruit_bag:
        return []
    # Processing
    temp = []
    for i in fruit_bag:
        i = i.replace("rotten", "", 1)
        i = i.lower()
        temp.append(i)
    return temp
