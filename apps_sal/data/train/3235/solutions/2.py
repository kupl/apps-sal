def decompose_single_strand(s):
    F1 = []
    F2 = [s[0]]
    F3 = [s[:2]]
    for i in range(0, len(s), 3):
        F1.append(s[i:i + 3])
    F1 = ' '.join(F1)
    for i in range(1, len(s), 3):
        F2.append(s[i:i + 3])
    F2 = ' '.join(F2)
    for i in range(2, len(s), 3):
        F3.append(s[i:i + 3])
    F3 = ' '.join(F3)
    return 'Frame 1: ' + F1 + '\n' + 'Frame 2: ' + F2 + '\n' + 'Frame 3: ' + F3
