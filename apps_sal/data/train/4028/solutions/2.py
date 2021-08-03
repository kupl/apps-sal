def riders(s, x):
    station, i, riders, p = 1, 0, [0], 0
    while station <= len(s) + 1:
        if riders[p] + s[i] <= 100:
            riders[p] += s[i]
        else:
            riders.append(0)
            p += 1
            continue
        station += 1
        i += 1
        if station == x:
            riders.append(0)
            p += 1
            i -= 1
            riders[p] += s[i]
    return len(riders)
