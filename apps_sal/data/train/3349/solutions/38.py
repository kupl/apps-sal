def find_missing_number(sequence):
    try:
        t=[int(i) for i in sequence.split()]
        st=set(range(1,len(t)+1))-set(t)
        return min(st) if st else 0
    except:
        return 1
