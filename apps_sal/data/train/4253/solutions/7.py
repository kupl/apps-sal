def solve(n,k):
    psum = (k * (k+1)) / 2
    if n >= psum:
        min_int = n // psum
        while min_int > 0:
            if n % min_int == 0:
                return populate(n,min_int,k)
            min_int -= 1
    return []

def populate(n,s,k):
    output = []
    m = n
    for i in range(1, k):
        output.append(i*s)
        m -= i*s
    output.append(m)
    return output

