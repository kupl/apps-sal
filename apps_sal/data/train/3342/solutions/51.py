def pattern(n):
    if n == 0:
        return ""
        
    return "\n".join([str(i)*i for i in range(n+1)][1:])

