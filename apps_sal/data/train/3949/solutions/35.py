import math
def calculate_tip(amount, rating):
    r = {'terrible':0, 'poor':0.05, 'good':0.1, 'great': 0.15, 'excellent':0.2}.get(rating.lower(), -1)
    return 'Rating not recognised' if r == -1 else math.ceil(amount*r) 
