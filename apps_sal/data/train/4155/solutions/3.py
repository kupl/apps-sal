def solve(a, b):
    return sum((n == n.translate(n.maketrans('2345679', '----9-6'))[::-1] for n in map(str, range(a, b))))
