def find(seq):
    prev = 0
    curr = 0
    seq.sort()
    
    length = len(seq)
    diff = (seq[length-1] - seq[0]) / length
    
    for i in range(1, len(seq)):
        
        
        if (seq[i]) == ((seq[curr])+diff):
            prev = curr
            curr = i

        
        else:
            return int(seq[curr]+diff)

        

