import math


def will_it_balance(stick, terrain):
    numerator = 0
    denominator = 0
    for index, weight in enumerate(stick):
        numerator += weight * (index + 1)
        denominator += weight
    centerOfMass = numerator / denominator
    centerOfMassLowCoord, centerOfMassHighCoord = math.floor(centerOfMass), math.ceil(centerOfMass)
    return terrain[centerOfMassLowCoord - 1] == 1 and terrain[centerOfMassHighCoord - 1] == 1
