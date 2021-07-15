def calculate_tip(amount, rating):
    import math
    tips = {'terrible': 1.0, 'poor': 1.05, 'good': 1.10, 'great': 1.15, 'excellent': 1.20}
    if rating.lower() in tips:
        return math.ceil(tips[rating.lower()] * amount - amount)
    else:
        return 'Rating not recognised'

