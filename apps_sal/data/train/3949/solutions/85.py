import math


def calculate_tip(amount, rating):
    calc_tip = {"terrible": 0, "poor": 0.05, "good": 0.10, "great": 0.15, "excellent": 0.20}
    if rating.lower() in calc_tip:
        res = amount * calc_tip[rating.lower()]
        if type(res) == float:
            res = math.ceil(res)
        return res
    else:
        return "Rating not recognised"
