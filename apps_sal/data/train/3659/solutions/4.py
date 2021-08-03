def mean(x):
    s = 0
    for i in range(len(x)):
        s = s + x[i]
    return s / len(x)


def variance(words):
    x = [len(word) for word in words]
    return round(mean([num**2 for num in x]) - mean(x)**2, 4)
