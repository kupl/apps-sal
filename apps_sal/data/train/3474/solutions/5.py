def pattern(n):
    return "1\n" + "\n".join(f"1{'*'*(i-1)}{i}" for i in range(2, n + 1))
