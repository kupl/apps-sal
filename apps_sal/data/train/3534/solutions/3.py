to_bits=lambda s:list(map(set(map(int,s.split('\n'))).__contains__,range(5000)))
