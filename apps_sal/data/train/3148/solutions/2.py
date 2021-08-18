def simplify(path):
    location = (0, 0)
    new_path = path
    new_path_locations = [location]

    for d in path:
        if d == '<':
            location = (location[0] - 1, location[1])
        elif d == '>':
            location = (location[0] + 1, location[1])
        elif d == 'v':
            location = (location[0], location[1] + 1)
        else:
            location = (location[0], location[1] - 1)

        if location in new_path_locations:
            i = new_path_locations.index(location)

            remove_length = len(new_path_locations) - i

            new_path_locations = new_path_locations[:i + 1]

            new_path = new_path[:i] + new_path[i + remove_length:]

        else:
            new_path_locations.append(location)

    return new_path
