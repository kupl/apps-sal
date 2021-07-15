def find_missing_number(sequence):
    try:
        return next((i for i,x in enumerate(sorted(map(int, sequence.split())), 1) if i != x), 0)
    except:
        return 1
