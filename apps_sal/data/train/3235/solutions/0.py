def decompose_single_strand(dna):        
    return '\n'.join('Frame {}: {}'.format(k+1, frame(dna, k)) for k in range(3))
    
def frame(s, k):
    return ' '.join(([s[:k]] if k else []) + [s[i:i+3] for i in range(k, len(s), 3)])    
