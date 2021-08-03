def find(n):
    def F(k):
        m = n // k
        return m * (m + 1) * k // 2

    return F(3) + F(5) - F(15)
