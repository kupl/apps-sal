def grid_index(ll, indexes):
    flatten = [item for flat_list in ll for item in flat_list]
    return "".join([flatten[index - 1] for index in indexes])
