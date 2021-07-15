def length_sup_u_k(n, k):
    return len(list(filter(lambda x: x >= k, create(n))))

def create(n):
    seq = []
    for i in range(n):
        seq.append(generate_term(i, seq))
    return seq
    
def generate_term(i, seq):
    if i == 0 or i == 1:
        return 1
    return seq[i - seq[i-1]] + seq[i - seq[i-2]]
    
def comp(n):
    count = 0
    seq = []
    for i in range(n):
        seq.append(generate_term(i, seq))
        if i != 0:
            if seq[i] < seq[i-1]:
                count += 1
    return count
