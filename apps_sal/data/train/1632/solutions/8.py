def countOnes(left, right):
    def bindig(number):
        ans = 0
        g = bin(number)[2:][::-1]
        for i in range(len(g)):
            if g[i] == '1':
                if i == len(g) - 1:
                    ans += 1 + ((2**(i - 1)) * i)
                else:
                    ans += 1 + (2**(i - 1)) * i + (g[i + 1:].count('1')) * (2**i)
        return ans
    return bindig(right) - bindig(left - 1)
