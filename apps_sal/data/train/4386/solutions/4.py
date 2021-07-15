def is_in_middle(sequence):
    while len(sequence) >= 3:        
        if sequence == 'abc' or sequence[1:] == 'abc' or sequence[:-1] == 'abc':
            return True
        sequence = sequence[1:-1]     
    return False
