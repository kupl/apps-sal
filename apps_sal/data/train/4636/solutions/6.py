def tv_remote(words):
    page1 = {'a': [0, 0], 'b': [0, 1], 'c': [0, 2], 'd': [0, 3], 'e': [0, 4], '1': [0, 5], '2': [0, 6], '3': [0, 7],
             'f': [1, 0], 'g': [1, 1], 'h': [1, 2], 'i': [1, 3], 'j': [1, 4], '4': [1, 5], '5': [1, 6], '6': [1, 7],
             'k': [2, 0], 'l': [2, 1], 'm': [2, 2], 'n': [2, 3], 'o': [2, 4], '7': [2, 5], '8': [2, 6], '9': [2, 7],
             'p': [3, 0], 'q': [3, 1], 'r': [3, 2], 's': [3, 3], 't': [3, 4], '.': [3, 5], '@': [3, 6], '0': [3, 7],
             'u': [4, 0], 'v': [4, 1], 'w': [4, 2], 'x': [4, 3], 'y': [4, 4], 'z': [4, 5], '_': [4, 6], '/': [4, 7],
             'aA#': [5, 0], ' ': [5, 1]}
    page2 = {'A': [0, 0], 'B': [0, 1], 'C': [0, 2], 'D': [0, 3], 'E': [0, 4], '1': [0, 5], '2': [0, 6], '3': [0, 7],
             'F': [1, 0], 'G': [1, 1], 'H': [1, 2], 'I': [1, 3], 'J': [1, 4], '4': [1, 5], '5': [1, 6], '6': [1, 7],
             'K': [2, 0], 'L': [2, 1], 'M': [2, 2], 'N': [2, 3], 'O': [2, 4], '7': [2, 5], '8': [2, 6], '9': [2, 7],
             'P': [3, 0], 'Q': [3, 1], 'R': [3, 2], 'S': [3, 3], 'T': [3, 4], '.': [3, 5], '@': [3, 6], '0': [3, 7],
             'U': [4, 0], 'V': [4, 1], 'W': [4, 2], 'X': [4, 3], 'Y': [4, 4], 'Z': [4, 5], '_': [4, 6], '/': [4, 7],
             'aA#': [5, 0], ' ': [5, 1]}
    page3 = {'^': [0, 0], '~': [0, 1], '?': [0, 2], '!': [0, 3], '\'': [0, 4], '"': [0, 5], '(': [0, 6], ')': [0, 7],
             '-': [1, 0], ':': [1, 1], ';': [1, 2], '+': [1, 3], '&': [1, 4], '%': [1, 5], '*': [1, 6], '=': [1, 7],
             '<': [2, 0], '>': [2, 1], '€': [2, 2], '£': [2, 3], '$': [2, 4], '¥': [2, 5], '¤': [2, 6], '\\': [2, 7],
             '[': [3, 0], ']': [3, 1], '{': [3, 2], '}': [3, 3], ',': [3, 4], '.': [3, 5], '@': [3, 6], '§': [3, 7],
             '#': [4, 0], '¿': [4, 1], '¡': [4, 2], '_': [4, 6], '/': [4, 7],
             'aA#': [5, 0], ' ': [5, 1]}

    pages = {1: page1, 2: page2, 3: page3}

    def move_to_page(position, current_page, target_page):
        moves = shortest_distance(position, [5, 0])
        if current_page == 3:
            if target_page == 1:
                moves += 1
            elif target_page == 2:
                moves += 2
        elif current_page == 2:
            if target_page == 1:
                moves += 2
            elif target_page == 3:
                moves += 1
        else:
            moves += target_page - current_page
        return moves

    def find_page(character):
        for page in pages:
            if character in pages[page]:
                return int(page)

    def shortest_distance(pos1, pos2):
        moves = 0
        delta_y = abs(pos2[0] - pos1[0])
        delta_x = abs(pos2[1] - pos1[1])
        return min(delta_x, 8 - delta_x) + min(delta_y, 6 - delta_y)

    debug = False
    sequence = list(words)
    moves = 0
    position = [0, 0]
    current_page = 1

    for element in sequence:
        if element not in pages[current_page]:
            target_page = find_page(element)
            moves += move_to_page(position, current_page, target_page)
            position = [5, 0]
            current_page = target_page
        target_position = pages[current_page][element]
        moves += shortest_distance(position, target_position)
        position = target_position
        moves += 1
    return moves
