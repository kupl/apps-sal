def most_frequent_item_count(collection):
    return max([collection.count(i) for i in collection]+[0])
