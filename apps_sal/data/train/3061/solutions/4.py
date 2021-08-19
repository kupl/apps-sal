def most_frequent_item_count(collection):
    return bool(collection) and max((collection.count(item) for item in set(collection)))
