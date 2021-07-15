def correct(m, n, bits):
    l = m*n
    row = next((i for i in range(m) if f"{bits[i*n:(i+1)*n]}{bits[l+i]}".count("1") % 2), None)
    col = next((i for i in range(n) if f"{bits[i:l:n]}{bits[l+m+i]}".count("1") % 2), None)
    if row is col is None:
        return bits
    err = (l + row) if col is None else (l + m + col) if row is None else (row * n + col)
    return f"{bits[:err]}{int(bits[err])^1}{bits[err+1:]}"

