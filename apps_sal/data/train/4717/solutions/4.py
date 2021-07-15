def pattern(n):
    if n < 1: return ""
    
    s = "1234567890" * (n//10 + 1)
    width = 2 * n - 1
    
    triangle = [(s[:i+1] + s[:i][::-1]).center(width) for i in range(n)]
    
    return "\n".join(triangle + triangle[:-1][::-1])
