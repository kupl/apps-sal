def split_all_even_numbers(numbers, way):
    def split0(n): return (n // 2, n // 2) if n//2 % 2 else (n//2 - 1, n//2 + 1)
    def split1(n): return 1, n-1
    def split2(n):
        ctr = 0
        while n % 2 == 0:
            ctr, n = ctr + 1, n//2
        return [n]*(2**ctr)
    def split3(n): return [1]*n
    split_ops = [split0, split1, split2, split3]
    return [x for lst in [split_ops[way](n) if n % 2 == 0 else [n] for n in numbers] for x in lst]
