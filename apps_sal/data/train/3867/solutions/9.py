def remove_rotten(bag):
    return [ fruit[6:].lower() if 'rotten' in fruit else fruit for fruit in bag] if bag else []
