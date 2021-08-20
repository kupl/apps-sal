def bubblesort_once(l):
    output = [i for i in l]
    for i in range(len(output) - 1):
        (output[i], output[i + 1]) = (min(output[i], output[i + 1]), max(output[i], output[i + 1]))
    return output
