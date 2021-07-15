def six_column_encryption(msg):
    row = (len(msg) + 5) // 6
    gen = iter(msg.replace(" ", "."))
    arr = zip(*[[next(gen, ".") for i in range(6)] for j in range(row)])
    return " ".join("".join(line) for line in arr)
