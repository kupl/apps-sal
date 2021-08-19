def calculate_tip(amount: int, rating: str) -> int:
    return {'Terrible': round((lambda x: x * 0.0)(amount) + 0.5), 'Poor': round((lambda x: x * 0.05)(amount) + 0.5), 'Good': round((lambda x: x * 0.1)(amount) + 0.5), 'Great': round((lambda x: x * 0.15)(amount) + 0.5), 'Excellent': round((lambda x: x * 0.2)(amount) + 0.5)}.get(rating.title(), 'Rating not recognised')
