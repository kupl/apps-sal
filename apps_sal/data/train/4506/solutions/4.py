def geometric_sequence_elements(a, r, n):
    return str([a*pow(r,i) for i in range(n)])[1:-1]
