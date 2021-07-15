def amidakuji(ar):
    results = [0 for i in range(len(ar[0]) + 1)]
    for i in range(len(ar[0]) + 1):
        pos = i
        for line in ar:
            move = False
            if pos > 0:
                if line[pos - 1] == '1':
                    pos -= 1
                    move = True
            if pos < len(line) and not move:
                if line[pos] == '1':
                    pos += 1
        results[pos] = i

    return results
