def modes(data):
    counts = {}
    for value in data:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    # return counts
    max_occurrence = max(counts.values())
    min_occurrence = min(counts.values())

    if max_occurrence == min_occurrence:
        return []
    result = []
    for key in counts.keys():
        if counts[key] == max_occurrence:
            result.append(key)
    return sorted(result)
