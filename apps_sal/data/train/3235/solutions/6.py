def decompose_single_strand(single_strand):
    string1 = [single_strand[i:i + 3] for i in range(0, len(single_strand), 3)]
    string2 = [single_strand[i:i + 3] if i != 0 else single_strand[i] for i in [0] + list(range(1, len(single_strand), 3))]
    string3 = [single_strand[i:i + 3] if i > 1 else single_strand[:i + 1] for i in [1] + list(range(2, len(single_strand), 3))]
    Frame = 'Frame 1: ' + ' '.join(string1) + '\nFrame 2: ' + ' '.join(string2) + '\nFrame 3: ' + ' '.join(string3)
    return Frame
