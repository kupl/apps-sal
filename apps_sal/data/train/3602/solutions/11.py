def run_length_encoding(s):
    rle = []
    for i, ch in enumerate(s):
        if i == 0:
            rle.append([1, ch])
        else:
            last_ch = rle[-1][1]
            if last_ch == ch:
                new_count = rle[-1][0] + 1
                rle.pop()
                rle.append([new_count, ch])
            else:
                rle.append([1, ch])
    return rle
