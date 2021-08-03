from math import log2, ceil
from decimal import Decimal

paper_thickness_meters = Decimal('0.0001')


def fold_to(distance):
    if distance < 0:
        return None
    elif distance < paper_thickness_meters:
        return 0
    layers = Decimal(str(distance)) / paper_thickness_meters
    return ceil(log2(layers))
