def modes(data):
    frequency = {}
    mode_list = []

    for d in data:
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1

    for f in frequency:
        if frequency[f] == max(frequency.values()) > min(frequency.values()):
            mode_list.append(f)

    return sorted(mode_list)
