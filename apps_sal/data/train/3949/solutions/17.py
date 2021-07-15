def calculate_tip(amount, rating):
  from math import ceil

  # Rating is case insensitive
  rating = rating.lower()

  ratingMap = {
    'terrible'  : 0.0,
    'poor'      : 0.05,
    'good'      : 0.10,
    'great'     : 0.15,
    'excellent' : 0.20
  }

  return ceil(amount * ratingMap[rating]) if rating in ratingMap else 'Rating not recognised'
