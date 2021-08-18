def check_left_hor(mat, row, col, r, c, z, diff):
    if 0 <= (z + diff) < c and mat[row][z + diff] == "L":

        for q in range(z + 1, z + diff):
            if mat[row][q] == "
            return False

        return True

    return False


def check_left_ver(mat, row, col, r, c, z, diff):
    if 0 <= (col + diff) < c and mat[z][col + diff] == "L":

        for q in range(col + 1, col + diff):
            if mat[z][q] == "
            return False

        return True

    return False


def check_right_hor(mat, row, col, r, c, z, diff):
    if 0 <= (z - diff) < c and mat[row][z - diff] == "R":

        for q in range(z - 1, z - diff, -1):
            if mat[row][q] == "
            return False

        return True

    return False


def check_right_ver(mat, row, col, r, c, z, diff):
    if 0 <= (col - diff) < c and mat[z][col - diff] == "R":

        for q in range(col - 1, col - diff, -1):
            if mat[z][q] == "
            return False

        return True

    return False


def check_down_hor(mat, row, col, r, c, z, diff):
    if 0 <= (row - diff) < r and mat[row - diff][z] == "D":

        for q in range(row - diff, row):
            if mat[q][z] == "
            return False

        return True

    return False


def check_down_ver(mat, row, col, r, c, z, diff):
    if 0 <= (z - diff) < r and mat[z - diff][col] == "D":

        for q in range(z - diff, z):
            if mat[q][col] == "
            return False

        return True

    return False


def check_up_hor(mat, row, col, r, c, z, diff):
    if 0 <= (row + diff) < r and mat[row + diff][z] == "U":
        for q in range(row + 1, row + diff):
            if mat[q][z] == "
            return False

        return True

    return False


def check_up_ver(mat, row, col, r, c, z, diff):

    if 0 <= (z + diff) < r and mat[z + diff][col] == "U":
        for q in range(z + 1, z + diff):
            if mat[q][col] == "
            return False

        return True

    return False


t = int(input())

for i in range(t):
    r, c = map(int, input().split())

    mat = []
    count = 0

    for j in range(r):
        temp = []
        s = input()

        for a in range(c):
            temp.append(s[a])
            if s[a] != "-" and s[a] != "
            count += 1

        mat.append(temp)

    meets = 0

    for row in range(r):

        for col in range(c):

            if mat[row][col] == "-" or mat[row][col] == "
            continue

            else:

                if mat[row][col] == "U":

                    for z in range(row - 1, -1, -1):
                        if mat[z][col] == "
                        break

                        else:
                            diff = row - z
                            if check_left_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_right_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_down_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                if mat[row][col] == "D":

                    for z in range(row + 1, r):
                        if mat[z][col] == "
                        break

                        else:
                            diff = z - row
                            if check_left_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_right_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_up_ver(mat, row, col, r, c, z, diff):
                                meets += 1

                if mat[row][col] == "L":

                    for z in range(col - 1, -1, -1):
                        if mat[row][z] == "
                        break

                        else:
                            diff = col - z
                            if check_down_hor(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_right_hor(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_up_hor(mat, row, col, r, c, z, diff):
                                meets += 1

                if mat[row][col] == "R":

                    for z in range(col + 1, c):
                        if mat[row][z] == "
                        break

                        else:
                            diff = z - col
                            if check_down_hor(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_left_hor(mat, row, col, r, c, z, diff):
                                meets += 1

                            if check_up_hor(mat, row, col, r, c, z, diff):
                                meets += 1

    print(meets // 2)
