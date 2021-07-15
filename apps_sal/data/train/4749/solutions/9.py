def base_finder(seq):
    mx = [int(char) for char in seq]
    mx = sorted(mx)
    print(mx)
    for i in range(min(mx), max(mx)):
        if i not in mx:
            return int(str(i)[-1])
    return len(mx)
