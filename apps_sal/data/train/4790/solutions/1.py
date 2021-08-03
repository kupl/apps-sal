from statistics import mean, pstdev


def clean_mean(sample, cutoff):
    cond = True
    while cond:
        _mean = mean(sample)
        _stdev = pstdev(sample)
        cut = [x for x in sample if abs(x - _mean) / _stdev <= cutoff]
        cond = len(sample) != len(cut)
        sample = cut
    return round(mean(sample), 2)
