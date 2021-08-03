def processes(start, end, processes):
    sequences = [[start, []]]
    while len(sequences) > 0:
        k = sequences[0]
        del sequences[0]
        node = k[0]
        path = k[1]
        if node == end:
            return path
        for n in processes:
            if n[1] == node and n[0] not in path:
                sequences.append([n[2], path + [n[0]]])
    return []
