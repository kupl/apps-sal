def add_binary(a, b):
    # your code here
    tot = a + b
    i = 0
    binsum = ''

    while i < i + 1:

        if tot >= 2**i and tot < 2**(i + 1):
            binsum = binsum + '1'
            tot = tot - 2**i

            for j in range(i - 1, -1, -1):

                if tot < 2**j:
                    binsum = binsum + '0'
                else:
                    binsum = binsum + '1'
                    tot = tot - 2**j
            break
        i += 1

    return binsum


print(add_binary(43, 11))
