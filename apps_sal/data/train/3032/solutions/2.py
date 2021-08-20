def factorsRange(n, m):

    def factors(n):
        ret = [i for i in range(2, n) if n % i == 0]
        if not ret:
            return ['None']
        return ret
    return {i: factors(i) for i in range(n, m + 1)}
