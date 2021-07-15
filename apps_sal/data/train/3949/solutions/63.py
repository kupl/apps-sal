import math

rates = {
    'terrible': 0,
    'poor': 0.05,
    'good': 0.1,
    'great': 0.15,
    'excellent': 0.2
}

def calculate_tip(amount, rating):
    rating = rating.lower()
    
    return math.ceil(amount * rates[rating]) if rating in rates else 'Rating not recognised'

