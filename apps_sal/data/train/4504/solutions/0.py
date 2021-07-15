def share_price(invested, changes):
    for change in changes:
        invested = invested * (100 + change) / 100.0
    return format(invested, '.2f')
