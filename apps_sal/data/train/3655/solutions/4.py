def my_crib(n):
    crib = [f"{mult(n-i)}/{mult(i*2)}\\{mult(n-i)}" for i in range(n)]
    crib.append(f"/{mult(n*2, '_')}\\")
    crib.extend(f"|{mult(n*2)}|" for _ in range(n - 1))
    crib.append(f"|{mult(n*2, '_')}|")
    return "\n".join(crib)


def mult(n, char=" "):
    return char * n
