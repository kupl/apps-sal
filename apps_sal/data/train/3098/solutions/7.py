def compute_depth(n):
    found = set()
    mult = 1
    while not set(x for x in range(0,10)) == found:
        for digit in str(n*mult):
            found.add(int(digit))
        mult += 1
    return mult-1
