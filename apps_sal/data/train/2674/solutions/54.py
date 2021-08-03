def two_sort(array):
    out = ""
    for let in sorted(array)[0]:
        out += let + "***"
    return out.rstrip("***")
