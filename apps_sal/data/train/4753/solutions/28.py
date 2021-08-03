geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    filtered_list = []
    for x in birds:
        if x not in geese:
            filtered_list.append(x)
    return (filtered_list)
