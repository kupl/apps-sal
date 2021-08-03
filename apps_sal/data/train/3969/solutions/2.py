def graceful_tipping(bill):
    import math
    multiple = 0
    tip = bill + (0.15 * bill)
    if tip < 10:
        multiple = 1
    elif tip < 100:
        multiple = 5
    elif tip < 1000:
        multiple = 50
    elif tip < 10000:
        multiple = 500
    elif tip < 100000:
        multiple = 5000
    elif tip < 1000000:
        multiple = 50000
    elif tip < 10000000:
        multiple = 500000
    elif tip < 100000000:
        multiple = 5000000

    return math.ceil(float(tip) / multiple) * multiple
