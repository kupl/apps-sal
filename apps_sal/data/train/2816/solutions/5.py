def calculate(s):
    
    oper = []
    for c in s:
        if c == 'p':
            oper.append('+')
        if c == 'm':
            oper.append('-')
    
    s = s.replace("plus", ' ')
    s = s.replace("minus", ' ')
    s = s.split(" ")
    
    result = int(s[0])
    
    for i in range(len(oper)):
        if oper[i]=='+':
            result += int(s[i+1])
        else:
            result -= int(s[i+1])
    
    return str(result)
