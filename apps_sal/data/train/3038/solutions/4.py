def solve(st):
    # Create a dictionary. Add every new char to dictionary. Check if that char is elsewhere in the
    # string. if it is, assign the value to the distance from each other.
    # If that char has the greatest distance, return that char.
    # If equal with others, return .isalpha

    # first_seen = {"a": 0, "b":2, "c":3}
    first_seen = {}
    distance = {}
    #distance = {"a": 1,"b":2, "c": 2, d:2}

    for index, char in enumerate(st):
        if char not in first_seen:
            first_seen[char] = index

        distance[char] = index - first_seen[char]

    # max = 2
    max = distance[st[0]]
    # max = b
    max_char = st[0]

    for key in distance:
        if distance[key] > max:
            max = distance[key]
            max_char = key
        elif distance[key] == max:
            if key < max_char:
                max_char = key

    return max_char
