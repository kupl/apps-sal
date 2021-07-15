def trace(mx):
    return None if not mx or len(mx) != len(mx[0]) else sum(mx[i][i] for i in range(len(mx)))
