def calculate_tip(amount, rating):
    import math
    r = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}
    if not rating or rating.lower() not in r:
        return 'Rating not recognised'
    else:
        return math.ceil(amount * r[rating.lower()] / 100.0)
