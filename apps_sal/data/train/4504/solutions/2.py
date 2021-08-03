def share_price(invested, changes):
    for change in changes:
        invested = invested + (invested * (change / 100.00))
    return "%.2f" % invested
