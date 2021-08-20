def covered_pawns(pawns):
    count = 0
    for i in range(len(pawns)):
        (x, y) = list(pawns[i])
        if ''.join([chr(ord(x) - 1), str(int(y) - 1)]) in pawns or ''.join([chr(ord(x) + 1), str(int(y) - 1)]) in pawns:
            count += 1
    return count
