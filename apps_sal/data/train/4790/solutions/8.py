from statistics import mean, pstdev

def clean_mean(sample, cutoff):
    n = 0
    while n != len(sample):
        n = len(sample)
        mu = mean(sample)
        sigma = pstdev(sample, mu)
        sample = [x for x in sample if abs(x - mu) < cutoff * sigma]
    return round(mu, 2)
