from re import sub


def remove_rotten(bag_of_fruits):
    return [sub('rotten', '', fruit).lower() for fruit in bag_of_fruits] if bag_of_fruits is not None else []
