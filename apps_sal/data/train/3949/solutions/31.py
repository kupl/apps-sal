from math import ceil
def calculate_tip(amount, rating): return ceil(amount * ["terrible", "poor", "good", "great", "excellent"].index(rating.lower()) * 0.05) if rating.lower() in ["terrible", "poor", "good", "great", "excellent"] else "Rating not recognised"
