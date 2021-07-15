more_zeros = lambda s: [x for x in {x:0 for x in s if bin(ord(x))[1:].count('0')>bin(ord(x))[1:].count('1')}]

