def almost_increasing_sequence(sequence):
    if len(sequence)>2:
        for i in range(len(sequence)-1):
            if sequence[i]>=sequence[i+1] and sequence[i+1]!=sequence[-1]:
                sequence.remove(sequence[i])
                for j in range(len(sequence)-1):
                    if sequence[j]>=sequence[j+1]:
                        return False
                return True
    return True
