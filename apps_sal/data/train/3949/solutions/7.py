from math import ceil


def calculate_tip(amount, rating):
    service = {"terrible": 0.00, "poor": 0.05, "good": 0.10, "great": 0.15, "excellent": 0.20}
    return(ceil(amount * service[rating.lower()]) if rating.lower() in service.keys() else "Rating not recognised")
