def ips_between(s, e): return sum((int(i[0]) - int(i[1])) * j for i, j in zip(zip(e.split('.'), s.split('.')), [16777216, 65536, 256, 1]))
