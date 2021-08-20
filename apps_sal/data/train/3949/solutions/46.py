def calculate_tip(amount, rating):
    ratings_dict = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}
    return int(amount / 100 * ratings_dict[rating.lower()] + 0.99) if rating.lower() in ratings_dict.keys() else 'Rating not recognised'
