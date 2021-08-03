def calculate_tip(amount, rating):
    d = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    try:
        return -(-amount * d[rating.lower()] // 1)
    except KeyError:
        return 'Rating not recognised'
