def automorphic(n):
    # your code here
    f = list(map(int, str(n)))
    z = list(map(int, str(n**2)))
    m = len(f)

    if f[:] == z[-m:]:
        return "Automorphic"
    else:
        return "Not!!"
