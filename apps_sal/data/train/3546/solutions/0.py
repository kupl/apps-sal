validate_ean = lambda code: (sum(map(int, code[0::2])) + sum(map(int, code[1::2])) * 3) % 10 == 0
