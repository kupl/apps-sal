def lose_weight(g, w, d): return "Invalid gender" if g not in "MF" else "Invalid weight" if w <= 0 else "Invalid duration" if d <= 0 else round(w * (0.985 if g == "M" else 0.988)**round(d), 1)
