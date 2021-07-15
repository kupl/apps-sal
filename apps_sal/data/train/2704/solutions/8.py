def almost_increasing_sequence(sequence):
    to_remove = 0
    min_ = sequence[0]
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            to_remove += 1
            if sequence[i+1] < min_ and min_ != sequence[i]:
                return False
            if to_remove == 2:
                return False
            min_ = sequence[i+1]
    return True
