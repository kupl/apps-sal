import math 
def calculate_tip(amount, rating):
    return math.ceil((amount*5)/100) if rating.lower() == "poor" else 0 if rating.lower() == "terrible" else math.ceil((amount*10)/100) if rating.lower() == "good" else math.ceil((amount*15)/100) if rating.lower() == "great" else math.ceil((amount*20)/100) if rating.lower() == "excellent" else "Rating not recognised"
