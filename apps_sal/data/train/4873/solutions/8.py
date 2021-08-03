def distance_between_points(a, b): return round(sum((a[0] - a[1])**2 for a in zip([a.x, a.y, a.z], [b.x, b.y, b.z]))**0.5, 6)
