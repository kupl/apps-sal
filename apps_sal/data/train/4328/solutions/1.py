def friend_find(line):
    N = len(line)
    A = lambda i: line[i] == "red" and B(i)
    B = lambda i: C(i) or D(i) or E(i)
    C = lambda i: i < N-2 and line[i+1] == line[i+2] == "blue"
    D = lambda i: 0 < i < N-1 and line[i-1] == line[i+1] == "blue"
    E = lambda i: 1 < i and line[i-2] == line[i-1] == "blue"
    return sum(map(A, range(N)))
