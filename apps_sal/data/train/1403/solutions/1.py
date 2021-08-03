t = int(input())
for i in range(t):
    def numDecodings(A):
        if A[0] == '0':
            return 0
        d = [0] * (len(A) + 1)
        d[0] = 1
        d[1] = 1
        for i in range(1, len(A)):
            g = int(A[i - 1] + A[i])
            if A[i] == '0' and (g != 10 and g != 20):
                return 0
            elif g == 10 or g == 20:
                d[i + 1] = d[i - 1]
            elif g > 10 and g <= 26:
                d[i + 1] = d[i] + d[i - 1]
            else:
                d[i + 1] = d[i]

        return d[len(A)] % 1000000007
    digits = input()
    print(numDecodings(digits))
