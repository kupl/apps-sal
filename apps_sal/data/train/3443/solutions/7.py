import pandas as pd


def correct(m, n, s):
    (s, r, c) = (s[:m * n], s[m * n:m * n + m], s[-n:])
    arr = pd.np.array(list(s)).reshape(m, n)
    df = pd.DataFrame(arr)
    row = ''.join(df.eq('1').sum(1).mod(2).astype(str))
    col = ''.join(df.eq('1').sum(0).mod(2).astype(str))
    if r != row and c != col:
        for (idx, (i, j)) in enumerate(zip(row, r)):
            if i != j:
                x = idx
        for (idx, (i, j)) in enumerate(zip(col, c)):
            if i != j:
                y = idx
        df = df.astype(int)
        df.loc[x, y] ^= 1
        return ''.join(df.astype(str).values.ravel()) + r + c
    else:
        return ''.join(df.values.ravel()) + row + col
