def fold_cube(number_list):
    print(number_list)
    connections = 0
    number_list.sort()

    for i in range(len(number_list)):
        if ((number_list[i] - 1) in number_list) and (number_list[i] not in [6, 11, 16, 21]):
            connections += 1
    for j in range(len(number_list)):
        if ((number_list[j] - 5) in number_list):
            connections += 1

    # in cube 6 faces are connected by 5 edges
    if connections != 5:
        return False

    horizontal = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    vertical = [[1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]

    lenghts_horizontal = []
    height = 0

    for h in horizontal:
        lh = 1
        any_in_row = False
        for i in range(len(number_list)):
            if number_list[i] in h:
                any_in_row = True
            if ((number_list[i] - 1) in number_list) and (number_list[i] in h) and (
                    number_list[i] not in [6, 11, 16, 21]):
                lh += 1
        if lh > 1:
            lenghts_horizontal.append(lh)
        elif any_in_row:
            lenghts_horizontal.append(1)
        if any_in_row:
            height += 1

    if lenghts_horizontal[0] == 4 or lenghts_horizontal[-1] == 4:
        return False

    is_3_horizontal_fist = False
    if lenghts_horizontal[0] == 3 or lenghts_horizontal[-1] == 3:
        is_3_horizontal_fist = True

    lenghts_horizontal.sort(reverse=True)

    if lenghts_horizontal[0] > 4:
        return False

    width = 0
    lenghts_vertical = []

    for v in vertical:
        lv = 1
        any_in_row = False
        for i in range(len(number_list)):
            if number_list[i] in v:
                any_in_row = True
            if ((number_list[i] - 5) in number_list) and (number_list[i] in v):
                lv += 1
        if lv > 1:
            lenghts_vertical.append(lv)
        elif any_in_row:
            lenghts_vertical.append(1)
        if any_in_row:
            width += 1

    if height == 3 and width == 3:
        return False

    if lenghts_vertical[0] == 4 or lenghts_vertical[-1] == 4:
        return False

    is_3_vertical_first = False
    if (lenghts_vertical[0] == 3) or (lenghts_vertical[-1] == 3):
        is_3_vertical_first = True

    lenghts_vertical.sort(reverse=True)

    if is_3_vertical_first and height == 4:
        return False

    if is_3_horizontal_fist and width == 4:
        return False

    if lenghts_vertical[0] > 4:
        return False

    if (lenghts_vertical[0] == 3 and lenghts_vertical[1] == 3 and width == 2):
        return True

    if (lenghts_horizontal[0] == 3 and lenghts_horizontal[1] == 3 and height == 2):
        return True

    upper = False
    upper_list = [1, 2, 3, 4, 5]
    lower = False
    lower_list = [21, 22, 23, 24, 25]
    left = False
    left_list = [1, 6, 11, 16, 21]
    right = False
    right_list = [5, 10, 15, 20, 25]

    for n in number_list:
        if n in upper_list:
            upper = True
        if n in lower_list:
            lower = True
        if n in left_list:
            left = True
        if n in right_list:
            right = True

    if upper and lower:
        return False
    if right and left:
        return False

    if lenghts_vertical == [2, 2, 1, 1] and lenghts_horizontal == [3, 2, 1] and width == 3 and height == 4:
        return False

    if ((lenghts_vertical[0] == 3 and width == 4 and height != 2) or (
            lenghts_horizontal[0] == 3 and height == 4 and width != 2)) and (lenghts_vertical != [3, 1, 1, 1]):
        return True

    if (lenghts_vertical[0] == 4 and width == 3 and height != 2) or (
            lenghts_horizontal[0] == 4 and height == 3 and width != 2):
        return True

    if (lenghts_vertical[0] == 3 and height == 4 and width != 2) or (
            lenghts_horizontal[0] == 3 and width == 4 and height != 2):
        return True

    if (lenghts_vertical[0] == 4 and height == 3 and width != 2) or (
            lenghts_horizontal[0] == 4 and width == 3 and height != 2):
        return True

    if lenghts_vertical == [2, 2, 2] and lenghts_horizontal == [2, 2, 1, 1]:
        return True

    if lenghts_horizontal == [2, 2, 2] and lenghts_vertical == [2, 2, 1, 1]:
        return True

    return False
