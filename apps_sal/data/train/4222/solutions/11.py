def get_size(w, h, d):
    L = []
    if w == h == d:
        SA = 6 * (w**2)
        V = w**3
        L.append(SA)
        L.append(V)
    else:
        SA = 2 * (w * h + w * d + h * d)
        V = w * h * d
        L.append(SA)
        L.append(V)
    return L
