def remove_rotten(fruit_bag):
    if not fruit_bag:
        return []
    temp = []
    for i in fruit_bag:
        i = i.replace("rotten", "", 1)
        i = i.lower()
        temp.append(i)
    return temp
