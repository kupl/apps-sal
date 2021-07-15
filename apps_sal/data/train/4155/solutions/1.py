def solve(a, b):
    return sum(str(n) == str(n)[::-1].translate(str.maketrans('2345679', 'XXXX9X6')) for n in range(a, b))
