import numpy as np

def micro_world(bacteria, k):
    bacteria = np.array(sorted(bacteria))
    for index, j in enumerate(bacteria):
        if j < 0:
            continue
        for i in bacteria[index:]:
            if i > j and i <= j + k:
                bacteria[bacteria == j] = -1
                break
    return len(list(filter(lambda x: x > 0, bacteria)))
