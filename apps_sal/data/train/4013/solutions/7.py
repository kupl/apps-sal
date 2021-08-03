def spoonerize(w): return (lambda w: " ".join([w[1][0] + w[0][1:], w[0][0] + w[1][1:]]))(w.split(" "))
