def pattern(n):
    return "\n".join(f"1{'*'*i}{i+1}" if i else "1" for i in range(n))
