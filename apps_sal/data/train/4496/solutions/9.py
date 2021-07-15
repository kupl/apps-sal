def hamming_distance(a, b):
    return sum(abs(int(a[i]) - int(b[i])) for i in range(0, len(a)))
        
        

