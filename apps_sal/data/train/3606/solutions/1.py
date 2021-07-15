def find_pattern(seq):
    start, end = [], []
    for i in range(len(seq)-1):
        start.append(seq[i+1]-seq[i])
        end.append(seq[-1-i]-seq[-2-i])
        if not (len(seq)-1) % len(start) and start == end[::-1] and not len(set(start)) == 1:
            return start
    return [start[0]] if len(set(start)) == 1 else []
