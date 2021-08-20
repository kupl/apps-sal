def pick_peaks(arr):
    real = [arr[x] for x in range(len(arr) - 1) if arr[x] != arr[x + 1]]
    track = [x for x in range(len(arr) - 1) if arr[x] == arr[x + 1]]
    if real:
        real.append(arr[-1])
    pos = [x for x in range(1, len(real) - 1) if real[x] > real[x - 1] and real[x] > real[x + 1]]
    posn = [x + 1 for x in range(1)]
    peak = [real[x] for x in range(1, len(real) - 1) if real[x] > real[x - 1] and real[x] > real[x + 1]]
    new = []
    count = 0
    a = 0
    for i in range(len(real)):
        if arr[i + count] != real[i]:
            skip = 0
            while arr[i + count] != real[i]:
                count += 1
                skip += 1
            if new:
                new.append([i + new[-1][1], skip])
            else:
                new.append([i, skip])
    for j in range(len(new)):
        for k in range(len(pos)):
            if pos[k] >= new[j][0]:
                pos[k] = pos[k] + new[j][1]
    total = {'pos': pos, 'peaks': peak}
    return total
