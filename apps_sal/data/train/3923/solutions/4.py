def micro_world(bacteria, k):
    for i in list(bacteria):
        bacteria = [x for x in bacteria if not (i > x and i -k <= x) or x == i]
        
    return len(bacteria)
