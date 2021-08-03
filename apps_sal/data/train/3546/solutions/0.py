def validate_ean(code): return (sum(map(int, code[0::2])) + sum(map(int, code[1::2])) * 3) % 10 == 0
