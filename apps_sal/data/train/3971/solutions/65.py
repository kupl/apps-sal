def tidyNumber(n):
    z = [int(x) for x in str(n)]
    print(z)
    return all((v <= y for (v, y) in zip(z, z[1:])))
