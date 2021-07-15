how_much_water=lambda w,l,c:"Too much clothes" if c>2*l else ("Not enough clothes" if c<l else round(w*(1.1**abs(l-c)),2))
