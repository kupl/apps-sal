def calculate_tip(a, r):
    d = {'terrible': 0, 'poor': .05, 'good': .10, 'great': .15, 'excellent': .20}
    return int(d[r.lower()] * a + .99) if r.lower() in d else 'Rating not recognised'
