def arithmetic(a, b, operator):
    ans= 0
    while operator == "add":
        ans = a+b
        break
    while operator == "subtract":
        ans = a-b
        break
    while operator == "multiply":
        ans = a*b
        break
        
    while operator == "divide":
        ans = a/b
        break
    return ans
