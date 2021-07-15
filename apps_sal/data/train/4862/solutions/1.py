def put_the_cat_on_the_table(cat, room):
    try:
        ci, cj = cat
        if not (0 <= ci < len(room) and 0 <= cj < len(room[0])):
            return "NoCat"
        ti, tj = next((i, j) for i,row in enumerate(room) for j,x in enumerate(row) if x)
        return "{}{}".format("UD"[ti>ci]*abs(ti-ci), "LR"[tj>cj]*abs(tj-cj))
    except StopIteration:
        return "NoTable"
