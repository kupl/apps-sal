def isValid(formula):
    m = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    t = []

    def mat1_mat2():
        count = 0
        for i in formula:
            if i == 1:
                count += 1
            if i == 2:
                count += 1
        if count == 0:
            t.append(True)
        elif count == 1:
            t.append(True)
        else:
            t.append(False)

    def mat3_mat4():
        count = 0
        for i in formula:
            if i == 3:
                count += 1
            if i == 4:
                count += 1
        if count == 0:
            t.append(True)
        elif count == 1:
            t.append(True)
        else:
            t.append(False)

    def mat5_mat6():
        count = 0
        for i in formula:
            if i == 5:
                count += 1
            if i == 6:
                count += 1
        if count == 0:
            t.append(True)
        elif count == 1:
            t.append(False)
        else:
            t.append(True)

    def mat7_mat8():
        count = 0
        for i in formula:
            if i == 7:
                count += 1
            if i == 8:
                count += 1
        if count == 1:
            t.append(True)
        elif count == 2:
            t.append(True)
        else:
            t.append(False)
    mat1_mat2()
    mat3_mat4()
    mat5_mat6()
    mat7_mat8()
    return all(t)
