from math import ceil


def calculate_tip(amount, rating):
    dict_ = {'excellent': 0.2, 'great': 0.15, 'good': 0.1, 'poor': 0.05, 'terrible': 0}
    if rating.lower() in dict_:
        return ceil(amount * dict_[rating.lower()])
    else:
        return 'Rating not recognised'
