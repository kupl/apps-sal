import math

def calculate_tip(amount, rating):
    r = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20,        
    }
    
    p = r.get(rating.lower(), 'Rating not recognised')
    
    try:
        return math.ceil(amount * p / 100)
    except:
        return p
