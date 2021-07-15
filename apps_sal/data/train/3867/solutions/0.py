def remove_rotten(bag_of_fruits):
    return [x.replace('rotten', '').lower() for x in bag_of_fruits] if bag_of_fruits else []
