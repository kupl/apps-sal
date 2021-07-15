def pattern(n):
    string = ''
    for i in range(1, n+1):
        for j in range(1,i + 1):
            string += (str)(i)
            
        if(i !=n):
            string += '\n'
    return string
