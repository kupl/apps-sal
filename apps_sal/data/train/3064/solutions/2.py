def transpose(arr):
    tran_each = []
    tran_com = []
    if len(arr) > 0 and len(arr[0]) > 0:
        n_row = len(arr[0])
        n_col = len(arr)
        for j in range(n_row):
            for i in range(n_col):
                tran_each.append(arr[i][j])
            tran_com.append(tran_each)
            tran_each = []
        return tran_com
    elif len(arr) > 0:
        return [[]]
    else:
        return []
