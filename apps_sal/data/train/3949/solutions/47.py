def calculate_tip(amount, rating):
    from math import ceil
    if rating.lower() == 'terrible':
        return 0
    if rating.lower() == 'poor':
        return ceil(int(amount) / 100 * 5)
    if rating.lower() == 'good':
        return ceil(int(amount) / 100 * 10)
    if rating.lower() == 'great':
        return ceil(int(amount) / 100 * 15)
    if rating.lower() == 'excellent':
        return ceil(int(amount) / 100 * 20)
    else:
        return 'Rating not recognised'
