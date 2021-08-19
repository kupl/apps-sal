def calculate_tip(amount, rating):
    from math import ceil
    rating = rating.lower()
    ratingMap = {'terrible': 0.0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return ceil(amount * ratingMap[rating]) if rating in ratingMap else 'Rating not recognised'
