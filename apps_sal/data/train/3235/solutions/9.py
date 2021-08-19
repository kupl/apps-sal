def decompose_single_strand(single_strand):
    frame1 = []
    frame2 = [single_strand[0]]
    frame3 = [single_strand[0:2]]
    for i in range(0, len(single_strand) - 2, 3):
        frame1.append(single_strand[i:i + 3])
        frame2.append(single_strand[i + 1:i + 4])
        frame3.append(single_strand[i + 2:i + 5])
    return 'Frame 1: {}\nFrame 2: {}\nFrame 3: {}'.format(' '.join(frame1), ' '.join(frame2), ' '.join(frame3))
