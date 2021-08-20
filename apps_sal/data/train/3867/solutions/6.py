def remove_rotten(bag_of_fruits):
    return [i[6:].lower() if i[:6] == 'rotten' else i for i in bag_of_fruits] if bag_of_fruits else []
