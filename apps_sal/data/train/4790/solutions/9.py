def clean_mean(sample, cutoff):
    if not sample:
        return 0
    samplesize = len(sample)
    print((samplesize, sample))
    mean = sum(sample) / samplesize
    stddev = ((samplesize ** -1) * sum((element - mean) ** 2 for element in sample)) ** 0.5
    cutoffpos = mean + cutoff * stddev
    cutoffneg = mean - cutoff * stddev
    for element in sample[:]:
        if element > cutoffpos or element < cutoffneg:
            sample.remove(element)
    if samplesize == len(sample):
        return round(mean, 2)
    else:
        return clean_mean(sample, cutoff)
        
    
    
    

