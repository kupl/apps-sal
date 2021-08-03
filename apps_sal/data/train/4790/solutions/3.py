from statistics import mean, pstdev


def clean_mean(sample, cutoff):
    u, v = mean(sample), pstdev(sample)
    cleaned = list(filter(lambda x: abs(x - u) <= cutoff * v, sample))
    if len(sample) == len(cleaned):
        return round(u, 2)
    return clean_mean(cleaned, cutoff)
