import numpy as np


def clean_mean(sample, cutoff):
    sample = np.array(sample)
    while True:
        m = np.mean(sample)
        newSample = sample[np.abs(sample - m) < cutoff * np.std(sample)]
        if len(sample) == len(newSample):
            return round(np.mean(newSample), 2)
        sample = newSample
