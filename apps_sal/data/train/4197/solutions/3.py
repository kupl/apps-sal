def top3(x, y, z):
    return [d[0] for d in sorted(list(zip(x, y, z)), key=lambda w: -w[1] * w[2])[:3]]
