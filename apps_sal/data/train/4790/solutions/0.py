def clean_mean(sample, cutoff):
    mean = sum(sample) / len(sample)
    dev = (1 / len(sample) * sum(((num - mean) ** 2 for num in sample))) ** (1 / 2)
    cleaned = [num for num in sample if abs(num - mean) <= cutoff * dev]
    if sample == cleaned:
        return round(mean, 2)
    else:
        return clean_mean(cleaned, cutoff)
