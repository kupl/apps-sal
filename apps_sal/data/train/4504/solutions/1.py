def share_price(invested, changes):
    sum = float(invested)
    for i in changes:
        sum = sum + (sum / 100 * i)
    return str('{:.2f}'.format(float(sum)))
