sumOnes = lambda n: (lambda msb: n and -~n + ~-msb * 2 ** msb + sumOnes(n - 2 ** -~msb))(n.bit_length() - 2)
countOnes = lambda a, b: sumOnes(b) - sumOnes(a-1)
