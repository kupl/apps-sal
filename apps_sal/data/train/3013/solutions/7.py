def delete_digit(n):
    n, i = str(n), 0
    while i < len(n)-1 and n[i] >= n[i+1]: i += 1
    return int(n[:i] + n[i+1:])
