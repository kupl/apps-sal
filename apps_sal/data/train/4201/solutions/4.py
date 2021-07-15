def find_missing(sequence):
    totalGap=sequence[len(sequence)-1]-sequence[0]
    eachGap = totalGap/len(sequence)
    for i in range(len(sequence)-1):
        if sequence[i]+eachGap != sequence[i+1]:
            return sequence[i]+eachGap
