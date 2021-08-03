def how_much_water(w, l, c): return "Too much clothes" if c > 2 * l else ("Not enough clothes" if c < l else round(w * (1.1**abs(l - c)), 2))
