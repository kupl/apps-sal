s = single_digit = lambda n: n if n < 10else s(sum(map(int, bin(n)[2:])))
