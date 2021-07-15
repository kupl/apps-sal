from statistics import *
def clean_mean(sample, cutoff):
    prev_mn, mn, sd = None, mean(sample), pstdev(sample)
    while mn != prev_mn:
        sample = [e for e in sample if mn-cutoff*sd < e < mn+cutoff*sd]
        prev_mn, mn, sd = mn, mean(sample), pstdev(sample)
        
    return round(mn, 2)

