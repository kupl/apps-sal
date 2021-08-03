def remove_rotten(bag_of_fruits):
    if bag_of_fruits is None:
        return []

    clean_bag = []

    for fruit in bag_of_fruits:
        if "rotten" in fruit:
            clean_bag.append(fruit.replace("rotten", "").lower())
        else:
            clean_bag.append(fruit)

    return clean_bag
