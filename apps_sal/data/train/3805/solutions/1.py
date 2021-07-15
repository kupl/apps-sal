def histogram(v, w):
    return [sum(j in range(i, w+i) for j in v) for i in range(0, max(v)+1, w)] if v else []
