fuel_price = lambda l,p: round(l*(p-min(0.05*(l//2), 0.25)), 2)
