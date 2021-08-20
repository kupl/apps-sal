def friend_find(line):
    N = len(line)

    def A(i):
        return line[i] == 'red' and B(i)

    def B(i):
        return C(i) or D(i) or E(i)

    def C(i):
        return i < N - 2 and line[i + 1] == line[i + 2] == 'blue'

    def D(i):
        return 0 < i < N - 1 and line[i - 1] == line[i + 1] == 'blue'

    def E(i):
        return 1 < i and line[i - 2] == line[i - 1] == 'blue'
    return sum(map(A, range(N)))
