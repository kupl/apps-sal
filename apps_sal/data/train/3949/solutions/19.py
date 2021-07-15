from math import ceil

def calculate_tip(amount, rating):
  tips, rating = 'terrible poor good great excellent'.split(), rating.lower()
  return ceil(amount * tips.index(rating) * .05) if rating in tips else 'Rating not recognised'
