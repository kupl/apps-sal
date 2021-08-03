# cook your dish here
for _ in range(int(input())):
    [m, b] = [int(i) for i in input().split()]

    def E(m, b):
        if m < b:
            return E(b, m)
        if b == 0:
            return m
        return E(b, m % b)
    print(2 * E(m, b))
