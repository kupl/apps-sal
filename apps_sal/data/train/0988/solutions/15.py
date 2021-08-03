# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    bitCountOne = [0] * 31
    bitCountZero = [0] * 31
    for a in A:
        binA = bin(a)[2:][::-1]
        placeValue = -1
        for bit in binA:
            if bit == '1':
                bitCountOne[placeValue] += 1
            else:
                bitCountZero[placeValue] += 1
            placeValue -= 1

    binStr = ''
    for i in range(31):
        if bitCountOne[i] > bitCountZero[i]:
            binStr += '1'
        else:
            binStr += '0'

    X = int(binStr, 2)
    minSum = 0
    for a in A:
        minSum += X ^ a
    print(minSum)
