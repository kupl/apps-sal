calculate_tip = lambda a, r, p=["terrible", "poor", "good", "great", "excellent"]: int(a * p.index(r.lower()) * 0.05 + 0.99) if r.lower() in p else "Rating not recognised"
