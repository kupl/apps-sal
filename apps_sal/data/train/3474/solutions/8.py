def pattern(n):
    return '\n'.join(['1'+"*"*i+str(i+1)*(i!=0) for i in range(n)])
