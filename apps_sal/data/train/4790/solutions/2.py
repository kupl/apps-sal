from numpy import mean, std

def clean_mean(sample, cutoff):
    m, newMean = 1j, mean(sample)
    while m != newMean:
        m, sd = newMean, std(sample)
        sample = [s for s in sample if abs(s-m) < sd * cutoff]
        newMean = mean(sample)
    return round(newMean, 2)
