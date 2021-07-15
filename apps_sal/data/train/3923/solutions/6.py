def micro_world(bacteria, k):
    i = 0
    j = 1
    bacteria = sorted(bacteria)
    
    while i < len(bacteria) - 1:
        if bacteria[i] == bacteria [i+j]:
            j += 1
            if i + j > len(bacteria) - 1:
                break
        else:
            if bacteria[i] < bacteria[i+j] <= bacteria[i] + k:
                bacteria.remove(bacteria[i])
            else:
                i += 1
            j = 1
    
    return len(bacteria)
