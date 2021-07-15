def find_missing_number(sequence):
    if sequence=="":
        return 0
    sequence=sequence.split(" ")
    try:
        sequence=list(map( int       ,sequence))
        sequence.sort()
        maxi = max(sequence)
        for i in range(1,maxi+1):
            if i not in sequence:
                return i
    except ValueError:
        return 1
    return 0
