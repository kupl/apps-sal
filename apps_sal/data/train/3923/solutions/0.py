def micro_world(bacteria, k):
    return sum(1 for e in bacteria if not [j for j in bacteria if e<j<=e+k])

