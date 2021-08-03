def shared_bits(a, b): return sum(f"{a:16b}"[i] == f"{b:16b}"[i] == "1" for i in range(16)) > 1
