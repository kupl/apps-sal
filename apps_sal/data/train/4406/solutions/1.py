def tram(stops, descending, onboarding):
    return max(sum(onboarding[:i])-sum(descending[:i]) for i in range(stops+1))

