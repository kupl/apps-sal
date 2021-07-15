def friends(n):
    return len(str(bin(n-1)))-3 if n >1 else 0
