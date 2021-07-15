def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0
