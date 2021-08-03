def loneliest(number):
    ints = [int(n) for n in str(number)]
    scores = [(sum(ints[max(0, i - d):i + d + 1]) - d, d)
              for i, d in enumerate(ints)]
    return (min(scores)[0], 1) in scores
