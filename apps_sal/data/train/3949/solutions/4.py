def calculate_tip(a, r):
    d = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return int(d[r.lower()] * a + 0.99) if r.lower() in d else 'Rating not recognised'
