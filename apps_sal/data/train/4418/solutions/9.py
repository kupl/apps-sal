def get_function(seq):
    if len(set([seq[i+1]-seq[i] for i in range(len(seq)-1)])) != 1:
        return 'Non-linear sequence'
    return lambda x: x*(seq[1]-seq[0])+seq[0]
