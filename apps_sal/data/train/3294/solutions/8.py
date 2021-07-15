def converter(mpg):
  L_PER_G = 4.54609188 # L
  KM_PER_MI = 1.609344 # km
  return round(mpg * KM_PER_MI / L_PER_G, 2)
