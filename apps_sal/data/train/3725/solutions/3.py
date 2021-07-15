def shift_left(a, b):
    return min(i+j for i in range(len(a)+1) for j in range(len(b)+1) if a[i:] == b[j:])
