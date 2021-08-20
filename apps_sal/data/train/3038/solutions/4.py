def solve(st):
    first_seen = {}
    distance = {}
    for (index, char) in enumerate(st):
        if char not in first_seen:
            first_seen[char] = index
        distance[char] = index - first_seen[char]
    max = distance[st[0]]
    max_char = st[0]
    for key in distance:
        if distance[key] > max:
            max = distance[key]
            max_char = key
        elif distance[key] == max:
            if key < max_char:
                max_char = key
    return max_char
