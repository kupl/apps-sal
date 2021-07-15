class Collatz(object):
    def __init__(self):
        self.memory = {1: 1}

    def calculate(self, n):
        if n in self.memory:
            return self.memory[n]

        result = self.calculate(n // 2) + 1 if n % 2 == 0 else self.calculate(3 * n + 1) + 1
        self.memory[n] = result
        return result


def max_collatz_length(n):
    if not isinstance(n, int) or n <= 0 or isinstance(n, bool):
        return []
    m = 0
    z = 0
    collatz = Collatz()
    for i in range(1, n + 1):
        c = collatz.calculate(i)
        if c > m:
            m = c
            z = i
    return [z, m]
