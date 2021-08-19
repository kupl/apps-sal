def countOnesFromZero(num):
    l = sorted([i for i, v in enumerate(bin(num)[2:][::-1]) if v == '1'], reverse=True)
    l.append(0)
    return sum(i * 2**v + v * 2**(v - 1) for i, v in enumerate(l))


def countOnes(left, right):
    # Your code here!
    return countOnesFromZero(right) - countOnesFromZero(left) + bin(left).count('1')
