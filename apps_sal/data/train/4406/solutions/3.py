def tram(stops, descending, onboarding):
    min_capacity, passengers = 0, 0
    for (off, on) in zip(descending[:stops], onboarding[:stops]):
        passengers += on - off
        min_capacity = max(min_capacity, passengers)
    return min_capacity
