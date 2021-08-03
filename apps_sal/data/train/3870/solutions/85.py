
def solve(s):
    s = list(s)
    indices = [index for index, element in enumerate(s) if element == " "]
    s = "".join(s).split()
    s = "".join(s)
    s = list(s[::-1])
    for i in range(0, 299):
        for j in indices:
            if i == j:
                s.insert(j, " ")

    return "".join(s)
