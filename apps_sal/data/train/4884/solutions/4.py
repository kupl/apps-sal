def connect_the_dots(paper):
    paper_list = list(paper)
    lines = paper.split('\n')
    len_line = len(lines[0]) + 1
    coords = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        found = False

        for row_index in range(len(lines)):
            try:
                column_index = lines[row_index].index(letter)
                found = True
                coords.append((row_index, column_index))
            except:
                pass

        if not found:
            break

    for i in range(1, len(coords)):
        from_x = coords[i-1][0]
        to_x = coords[i][0]
        from_y = coords[i-1][1]
        to_y = coords[i][1]

        step_x = 1
        step_y = 1

        if from_x == to_x:
            step_x = 0
        if from_x > to_x:
            step_x = -1
        if from_y == to_y:
            step_y = 0
        if from_y > to_y:
            step_y = -1

        for _ in range(1 + max(from_x-to_x, to_x-from_x,from_y-to_y,to_y-from_y)):
            paper_list[from_y + (from_x * len_line)] = '*'
            from_x += step_x
            from_y += step_y


    return "".join(paper_list)
